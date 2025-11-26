from django.shortcuts import render,redirect
from .models import Question, Choice



def quiz(request):

    questions = Question.objects.all().prefetch_related('choices')

    if request.method == "POST":
        
        score = 0                                                                                        # initially score is 0
        for question in questions:                                                                       # loop used to check each question's submitted answer is right/wrong

            selected = request.POST.get(str(question.id))                                                  # getting the option selected by the user; converting the dictionary as string; --> {1: 2, 2: 3}
            correct = Choice.objects.filter(id = selected, is_correct = True).exists()                     # checking if the choice it correct or not; (it has to be selected + is_correct=True in DB)--> correct


            if correct:
                score+=1                                                                                # correct ans increases the score
            
        return render(request, 'score.html', context={
        'total_question' : len(questions),
        'score' : score
    })
           

    return render(request, 'quiz.html', context={
        'questions': questions
    })                                                                  # context used to pass the questions to html




