## Problem Statement
'''
Function that returns the possible time available for meeting bw two workers.
Given the meetings timings and daily time bounds of two workers and the new meeting time(in mins) 

Ex :  calendar1   = [["9:00", "10:30"],["12:00", "13:00"],["16:00", "18:00"]]
      dailyBound1 = ["9:00", "20:00"]
      calendar2   = [["10:00", "11:30"],["12:30", "14:30"],["14:30", "15:00"],["16:00", "17:00"]]
      dailyBound2 = ["10:00", "18:30"]
      meetingDuration = 30mins (minimum)
    
      Answer : [["11:30","12:00"],["15:00","16:00"],["18:00","18:30"]]

'''
### Solution -1
## Time - O(c1+c2)    |  Space - O(c1+c2) 

def hourToMins(strtime):
      hours , mins = list(map(int,strtime.split(":")))
      return hours * 60 + mins

def minsToHour(minutes):
      hour = str(minutes // 60)
      mins = minutes % 60
      mins = "0"+str(mins) if mins < 10 else str(mins)

      return hour + ":"+ mins

def updateCalendar(calendar,dailyBound):
      updateCalendar = calendar[:]
      updateCalendar.insert(0,["0:00",dailyBound[0]])
      updateCalendar.append([dailyBound[1],"23:59"])

      return list(map(lambda m:[hourToMins(m[0]),hourToMins(m[1])], updateCalendar))


def mergeCalendar(calendar1,calendar2):
      merged = []
      i,j = 0,0

      while i < len(calendar1)  and j < len(calendar2):
            meeting1 , meeting2 = calendar1[i], calendar2[j]
            if meeting1[0] < meeting2[0]:
                  merged.append(meeting1)
                  i += 1
            else:
                  merged.append(meeting2)
                  j += 1

      while i < len(calendar1):
            merged.append(calendar1[i])
            i += 1
      while j < len(calendar2):
            merged.append(calendar2[j])
            j += 1
      
      return merged


def getFlattenCalendar(calendar):
      flattened = [calendar[0][:]]

      for i in range(len(calendar)):
            currentMeeting  = calendar[i]
            previousMeeting = flattened[-1]
            currentStart, currentEnd = currentMeeting
            previousStart, previousEnd = previousMeeting

            if previousEnd >= currentStart :
                  newPreviousMeeting = [previousStart,max(previousEnd,currentEnd)]
                  flattened[-1] = newPreviousMeeting
            else:
                  flattened.append(currentMeeting[:])
      
      return flattened


def getMatchingAvailabilities(calendar,meetingDuration):
      matchingTimes = []

      for i in range(1,len(calendar)):
            startTime = calendar[i-1][1]
            endTime = calendar[i][0]
            if endTime - startTime >= meetingDuration :
                  matchingTimes.append([startTime,endTime])

      return list(map(lambda m : [minsToHour(m[0]),minsToHour(m[1])], matchingTimes))


def calendarMatching(calendar1,dailyBound1,calendar2,dailyBound2,meetingDuration):

      updatedCalendar1 = updateCalendar(calendar1,dailyBound1)
      updatedCalendar2 = updateCalendar(calendar2,dailyBound2)
      mergedCalendar  = mergeCalendar(updatedCalendar1,updatedCalendar2)
      flattenCalendar = getFlattenCalendar(mergedCalendar)
      matchingCalendar = getMatchingAvailabilities(flattenCalendar,meetingDuration)
      return matchingCalendar

calendar1   = [["9:00", "10:30"],["12:00", "13:00"],["16:00", "18:00"]]
dailyBound1 = ["9:00", "20:00"]
calendar2   = [["10:00", "11:30"],["12:30", "14:30"],["14:30", "15:00"],["16:00", "17:00"]]
dailyBound2 = ["10:00", "18:30"]
meetingDuration = 30

print(calendarMatching(calendar1,dailyBound1,calendar2,dailyBound2,meetingDuration))

    