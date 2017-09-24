from polls.models import Question,Choice

q1= Question(question_text="What is your name?")
q1.save()

q2 = Question(question_text="Are you studying?")
q2.save()

q3 = Question(question_text="Is that an apple?")
q3.save()


q= Question.objects.get(pk=1)

q.choice_set.all()

choice_text = ["Naveen","Krishna","Murakonda"]
votes = [0,1,0]


for i in range(len(votes)):
	q.choice_set.create(choice_text=choice_text[i],votes=votes[i])

q= Question.objects.get(pk=2)


choice_text = ["yes","no"]
votes = [0,1]

for i in range(len(votes)):
	q.choice_set.create(choice_text=choice_text[i],votes=votes[i])


q= Question.objects.get(pk=3)


choice_text = ["yes","no"]
votes = [0,1]

for i in range(len(votes)):
	q.choice_set.create(choice_text=choice_text[i],votes=votes[i])
