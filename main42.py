class dad:

    basketball=1

class son(dad):

   dance = 1
   def isdance(self):
       return f"yes i dance {self.dance} no of times"
class grandson(son):
    dance=7
    basketball = 8
    def isdance(self):
        return f"jack son yeah!"\
            f"yes i dance very awesomly {self.dance} no of times"
delhi= dad()
mumbai=son()
hyderabad=grandson()
print(hyderabad.isdance())
print(hyderabad.basketball)