"""
FIT2004 ASSIGNMENT 1 
 Syed Zubin Hafiz
 ID: 32227671
 
"""

def analyze (results,roster,score) : 
    #Input :
        # results : a list containing two teams composed of letters of the English alphabet and their score 
                    # format : [[team1,team2,score]]
                    # team1 and team2 are always composed with capital letters, e.g: ['ABC','BCD',20]
        # roster: a numerical value which denotes how many distinct letters a team may be composed of
                    # eg 5 represents ["A","B","C","D","E"]
        # score: a numerical value between 0-100 inclusive, which shows how much team 1 scored against team 2
    
    # Output : 
        # top10matches: matches with highest score
                        # descending order by score, ascending lexicographical order for team1, ascending lexicographical order for team2
                        # if matches with same teams with same score, include one (if same team diff scores, include both)
                        # if < 10 matches, contain max matches possible
                        # assume always at least one match returned in top10matches
        #searchedmatches: : list of matches with same score as score
                            # ascending lexicographical order for team 1, ascending lexicographical order for team 2
                            # if matches between same team, include one and remove the duplicate
                            # if score not found, return closest score that's higher (if not available, return empty list)
        
    # Time Complexity: 
        # Time Complexity for radix sort of strings : O(MN)
        # Time Complexity for radix sort of scores: O(N)
    top10matches = []
    searchedmatches = []
    
    # Add all the reverses to results
    reverses = []
    for (team1, team2, scr) in results:
        # (team2, team1, 100-score)
        reverses.append([team2, team1, 100-scr])
    results += reverses
    
    # Make every string alphabetical: Time & Space Complexity: O(1)
    for i in [0,1]:
        for match in results:
            charList = []
            charList = [j for j in match[i]]
            charStr = "".join(counting_string_sort_normal(charList,0))
            match[i] = charStr
              
    # Radix sort both teams and their scores
    results = radix_string_sort(results,1) # team2    
    results = radix_string_sort(results,0) # team1    
    results = radix_int_sort(results) #score   
         
    # Remove duplicates from results
    results = removeDuplicates(results)
    
    # Get top 10 matches
    topCount = min(10,len(results))
    top10matches = results[-topCount:]
    top10matches.reverse()
    
    # Index of score (binary search)
    scoreIndex, score = binarySearch(results,score)
    
    # Get searchedmatches
    # if there are multiple matches with the searched score, find the item at the very right
    while(scoreIndex<len(results)-1 and results[scoreIndex+1][2]==score):
        scoreIndex += 1
    # add every match equal to the score into the searchedmatches array
    if(scoreIndex!=None):
        while(scoreIndex>=0 and results[scoreIndex][2]==score):
            searchedmatches.append(results[scoreIndex])
            scoreIndex -= 1
    return [top10matches,searchedmatches]

 
def removeDuplicates(result_lst):
    # input: list of scores
    # output: list with the duplicates removed
    # Space Complexity O(MN)
    # Time  Complexity O(kN)
    
    #How it works: 
    # Checks every element in the list one by one to find a match
    i = 0
    j = 0
    duplicates = 0
    while(i<len(result_lst)-1):
        while(j<len(result_lst)-1):
            if(result_lst[j]==result_lst[i+1]):
                i += 1
                duplicates += 1
            else:
                result_lst[j+1] = result_lst[i+1]
                i += 1
                j += 1
                
            if(i>=len(result_lst)-1): 
                break 
    if(duplicates==0):
        return result_lst 
    else:
        return result_lst[:-duplicates]

def binarySearch(arr,value,key=lambda x:x[2]):
# input: arr- a sorted list,value- the value to find, key-a function used to extract the value 
# that can be compared with the value parameter, at index 2
# output:the index of the value, or the next largest value if not found
# Time Complexity: O(log(N))
# Auxilary Space Complexity: O(1)

# How it works:
# If the value of the search key is equal to the item then return an index of the search key.
# Or if the value of the search key is less than the item in the middle of the interval, narrow the interval to the lower half.
# Otherwise, narrow it to the upper half.
# Repeatedly check from the second point until the value is found or the interval is empty.
    if(value<key(arr[0])):
        return 0, key(arr[0])
    elif(value>key(arr[-1])):
        return len(arr)-1, None
    lo = 0
    hi = len(arr)-1
    mid = None
    while(lo <= hi):
        mid = (lo+hi)//2
        k = key(arr[mid])
        if(value==k):
            break
        elif(mid>0 and value<k and value>key(arr[mid-1])):
            break
        elif(value<k):
            hi = mid - 1
        else:
            lo = mid + 1
    if(key(arr[mid])<value):
        mid += 1
    while(mid<len(arr)-1 and arr[mid+1][2]==value):
        mid += 1
    return mid, key(arr[mid])

def counting_string_sort_normal(input_list,column): 
    # input: list of strings,column to sort
    # output: sorted list of strings
    # Time complexity: O(N)
    # Auxilary Space complexity: O(MN)
    
    #How it works:
    # Sorts the elements of an array by counting the number of occurrences of each unique element in the array. 
    # The count is stored in an auxiliary array(in this case count_array) and the sorting is done by mapping the count as an index of the auxiliary array.
    count_array = [None] * (26)
    for i in range(len(count_array)):
        count_array[i] = []
    # update count array
    for i in range(len(input_list)):
      req_char = ord((input_list[i][column]))-65
      count_array[req_char].append(input_list[i])   
    # Add sorted values to a temporary list and return  
    temp_input_list = [] 
    for string_input_list in count_array:
        for characters in string_input_list:
            temp_input_list.append(characters)
    return temp_input_list

    # Same algorithm as above, but modified for sorting in a reverse alphabetical order
def counting_string_sort(input_list,column,resultsColumn): 
    count_array = [None] * (26)
    for i in range(len(count_array)):
        count_array[i] = []
    # update count array
    for i in range(len(input_list)): # A = 0, Z = 25 --->  # Z = 0, A = 25
      req_char = ord((input_list[i][resultsColumn][column]))-65
      req_char = 26 - 1 - req_char
      count_array[req_char].append(input_list[i])   
    # Add sorted values to a temporary list and return  
    temp_input_list = [] 
    for string_input_list in count_array:
        for characters in string_input_list:
            temp_input_list.append(characters)
    return temp_input_list

    #Counting sort algorithm for integers
def counting_int_sort(input_list,column,resultsColumn):
    # input : the input list, the column to sort 
            # the result column where the integers exist
    # output: sorted list of numbers in descending order
    # Time Complexity : O(N)
    # Auxilary Space Complexity : O(MN)
    base = 10
    max_item = max([match[resultsColumn] for match in input_list])
    count_array = [None] * (max_item+1)
    for i in range(len(count_array)):
        count_array[i] = []
    # update count array
    for i in range(len(input_list)):
     req_digit = (input_list[i][resultsColumn] // base**column)%base 
     count_array[req_digit].append(input_list[i])   
    # Add sorted values to a temporary list and return   
    new_input_list = [] 
    for digits in count_array:
        for i in range (len(digits)):
            new_input_list.append(digits[i])
    return new_input_list

def radix_int_sort(radix_input_list,resultsColumn=2):
    #input : input list of integers, or in this case the scores, 
           # the resultsColumn where the scores are present in the list of lists, which is 2
    # output: the sorted list of integers after all the relevant columns are count-sorted and returned 
    
    # Time Complexity: O(MN)
    # Auxilary Space Complexity: O(MN) 
    
    #How it works: 
    # Instead of the input list being sorted as a whole, we flip it vertically and consider the columns.
    # We count-sort the columns and return the sorted column which is then appended back to the original list until the entire list is sorted
    max_digit = max(radix_input_list)
    col = 0
    while col < len(str(max_digit)):
        radix_input_list = counting_int_sort(radix_input_list, col,resultsColumn)
        col += 1
    return radix_input_list

def radix_string_sort(radix_input_list,resultsColumn):
     #input : input list of the team compositions 
            # the resultsColumn where the the two teams are present in the list of lists
    # output: the sorted list of strings after all the relevant columns are count-sorted and returned 
    
    # Time Complexity: O(MN)
    # Auxilary Space Complexity: O(MN) 
    max_digit = len(radix_input_list[0][resultsColumn])
    for match in radix_input_list:
        max_digit = max(max_digit,len(match[resultsColumn]))
    col = max_digit - 1
    while col >= 0:
        radix_input_list = counting_string_sort(radix_input_list, col,resultsColumn)
        col -= 1
    return radix_input_list
        
        
#----------------------------->DRIVER<--------------------------------
if __name__ == "__main__":
    # a roster of 2 characters
    roster = 2
    # results with 20 matches
    results = [
        ['AAB', 'AAB', 35], ['AAB', 'BBA', 49], ['BAB', 'BAB', 42],
        ['AAA', 'AAA', 38], ['BAB', 'BAB', 36], ['BAB', 'BAB', 36],
        ['ABA', 'BBA', 57], ['BBB', 'BBA', 32], ['BBA', 'BBB', 49],
        ['BBA', 'ABB', 55], ['AAB', 'AAA', 58], ['ABA', 'AAA', 46],
        ['ABA', 'ABB', 44], ['BBB', 'BAB', 32], ['AAA', 'AAB', 36],
        ['ABA', 'BBB', 48], ['BBB', 'ABA', 33], ['AAB', 'BBA', 30],
        ['ABB', 'BBB', 68], ['BAB', 'BBB', 52]
        ]
    # looking for a score of 64
    score = 64
    # running the function
    # analyze(results, roster, score)
    print(analyze(results, roster, score))