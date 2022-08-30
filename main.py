from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from art import logo

print(logo)

question_bank=[]

for question in question_data:
    question_text=question["question"]
    question_ans=question["correct_answer"]
    new_question=Question(question_text, question_ans)
    question_bank.append(new_question)
    # print(new_question)
    
# print(question_bank[0].text)
# print(question_bank[0].ans)

quiz=QuizBrain(question_bank)

 
  
while quiz.still_has_questions():
    quiz.next_question()
    # quiz.check_ans()
    
print("Well Played !! You have completed the quiz")  
print(f"Your final score is = {quiz.score}/{len(question_bank)}")

    


