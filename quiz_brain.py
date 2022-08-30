class QuizBrain:
    def __init__(self,question_list):
        self.quest_num=0
        self.question_list=question_list
        self.score=0
        
    def still_has_questions(self):
       return self.quest_num<len(self.question_list)
   
   
    def next_question(self):
        current_question = self.question_list[self.quest_num]
        self.quest_num += 1
        user_ans = input(f"Q.{self.quest_num}: {current_question.text} (True/False): ")
        self.check_ans(user_ans, current_question.ans)
             




    def check_ans(self,user_ans,correct_ans):
        
        if user_ans.lower()==correct_ans.lower():
            print("Correct !")
            self.score+=1
            print(f"Your score is : {self.score}/{self.quest_num}")
        else:
            print("Ooops !! That's not the right answer\n")
            print(f"Correct answer is {correct_ans} ")
            
            print(f"Your score is : {self.score}/{self.quest_num}\n")
            
                
                # exit()
                    