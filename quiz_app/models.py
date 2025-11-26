from django.db import models



# 2 Tables
# Question Table and Choice Table
# Question Table will have the Question
# Choice Table will have the 4 choices



# Question Model
# Just have the Question Only
class Question(models.Model):

    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text
    





# Choice Model
# 4 Choices
class Choice(models.Model):

    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')                    # 1 Question will have many Multiple Choices;  [[related_name='choices'-> backward relationship]-- used to kon question er jonno kon options

    text = models.CharField(max_length=255)                                             # the option

    is_correct = models.BooleanField(default=False)                                     # which field is correct; If not chosen then it will consider it as false



    def __str__(self):
        return self.text

