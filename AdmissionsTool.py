#Function: This program determines if a student will be admitted or rejected.

#Input:  Interactive

response1 = input("PLease enter student test score: ")



response2 = input("Please enter student class rank: ")



#Output: Accept or Reject
# Get input and convert to correct data type for testScore and classRank
# Test using admission requirements and print Accept or Reject
testScore = int(response1)

classRank = int(response2)

if testScore >= 90:
  if classRank >= 25:
    print("Accept")
  else:
    print("Reject")
else:
  if testScore >= 80:
    if classRank >= 50:
      print("Accept")
    else:
      print("Reject")
  else:
    if testScore >= 70:
      if classRank >= 75:
        print("Accept")
      else:
        print("Reject")
    else:
      print("Reject")
