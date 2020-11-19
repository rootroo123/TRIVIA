print ('Welcome To Trivia')
print ('topic: Jacob')
score = 0 
total_q = 3
ans=input ('what is Jacobs favorite color? purple/orange >')
if ans == 'purple':
  score+=1
  print ('Correct')
else:
  print ('incorrect')
ans=input ('what is Jacobs favorite food? hotdog/burger >')
if ans == 'burger':
  score+=1
  print ('correct')
else:
  print ('incorrect')
  print ('note no caps will be used')
ans=input ('Where does Jacob live? fiance/mom > ')
if ans == 'fiance':
  score+=1
  print ('correct')

mark = (score/total_q) * 100
print (mark)