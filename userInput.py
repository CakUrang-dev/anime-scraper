# User Choosing Genre
print(f'''
Choose the genre you want:
1. Action       14. Drama       24. Historical      34. Mecha
2. Demons       15. Hentai      25. Martial Arts    35. Police
3. Harem        16. Magic       26. Parody          36. Sci-Fi
4. Kids         17. Mystery     27. School          37. Shounen Ai
5. Music        18. Samurai     28. Shounen         38. Supernatural
6. Romance      19. Shoujo Ai   29. Super Power     39. Dementia
7. Shoujo       20. Sports      30. Yuri            40. Game
8. Space        21. Yaoi        31. Comedy          41. Josei
9. Vampire      22. Cars        32. Fantasy         42. Military
10. Adventure   23. Ecchi       33. Horror          43. Psychological
11. Seinen 
12. Slice of Life
13. Thriller
''')

input_number = input("Choose the number: ")
genre_link = ''
if input_number == "1":
    genre_link = "1/Action"
elif input_number == "2":
    genre_link = "6/Demons"
elif input_number == "3":
    genre_link = "35/Harem"
elif input_number == "4":
    genre_link = "15/Kids"
elif input_number == "5":
    genre_link = "19/Music"
elif input_number == "6":
    genre_link = "22/Romance"
elif input_number == "7":
    genre_link = "25/Shoujo"
elif input_number == "8":
    genre_link = "29/Space"
elif input_number == "9":
    genre_link = "32/Vampire"
elif input_number == "10":
    genre_link = "2/Adventure"
elif input_number == "11":
    genre_link = "42/Seinen"
elif input_number == "12":
    genre_link = "36/Slice_of_Life"
elif input_number == "13":
    genre_link = "41/Thriller"
elif input_number == "14":
    genre_link = "8/Drama"
elif input_number == "15":
    genre_link = "12/Hentai"
elif input_number == "16":
    genre_link = "16/Magic"
elif input_number == "17":
    genre_link = "7/Mystery"
elif input_number == "18":
    genre_link = "21/Samurai"
elif input_number == "19":
    genre_link = "26/Shoujo_Ai"
elif input_number == "20":
    genre_link = "30/Sports"
elif input_number == "21":
    genre_link = "33/Yaoi"
elif input_number == "22":
    genre_link = "3/Cars"
elif input_number == "23":
    genre_link = "9/Ecchi"
elif input_number == "24":
    genre_link = "13/Historical"
elif input_number == "25":
    genre_link = "17/Martial_Arts"
elif input_number == "26":
    genre_link = "20/Parody"
elif input_number == "27":
    genre_link = "23/School"
elif input_number == "28":
    genre_link = "27/Shounen"
elif input_number == "29":
    genre_link = "31/Super_Power"
elif input_number == "30":
    genre_link = "34/Yuri"
elif input_number == "31":
    genre_link = "4/Comedy"
elif input_number == "32":
    genre_link = "10/Fantasy"
elif input_number == "33":
    genre_link = "14/Horror"
elif input_number == "34":
    genre_link = "18/Mecha"
elif input_number == "35":
    genre_link = "39/Police"
elif input_number == "36":
    genre_link = "24/Sci-Fi"
elif input_number == "37":
    genre_link = "28/Shounen_Ai"
elif input_number == "38":
    genre_link = "37/Supernatural"
elif input_number == "39":
    genre_link = "5/Dementia"
elif input_number == "40":
    genre_link = "11/Game"
elif input_number == "41":
    genre_link = "43/Josei"
elif input_number == "42":
    genre_link = "38/Military"
elif input_number == "43":
    genre_link = "40/Psychological"
else:
    print("Error")