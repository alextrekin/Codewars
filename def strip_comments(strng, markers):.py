def strip_comments(strng, markers):
    i=0 
    el = 0
    exam=0
    start_text = ""
    while i < len(markers):
        el = strng.find(markers[i])
        if el == -1:
            i+=1
        else:
            if strng[el-1] == " ":
                start_text += strng[:el-1]
            else:
                start_text+=strng[:el]
            if strng.find("\n",el) != -1:
                strng = strng[strng.find("\n",el):]
            else:
                strng = ""
            strng = start_text+strng
    print(strng)

#запуск программы
strng = '  ? lemons watermelons avocados\n- avocados # lemons -\nwatermelons\n^ lemons cherries'
markers = ['=', '.', "'", '^', '#']
strip_comments(strng,markers)