inp_date = input()

def is_input_valid(inp_date):
    if inp_date[5:7] == "02" and inp_date[8:10] == "28":
        inp_date = inp_date[:5] + "03-01"
    if inp_date[4] != "-" or inp_date[7] != "-":
        print("Input format ERROR. Correct Format: YYYY-MM-DD")
    if inp_date[5:7] == "12" and inp_date[8:10] == "31":
        inp_date = str(int(inp_date[0:4]) + 1) + "-01-01"
    if (inp_date[5:7] in ["04", "06", "09", "11"]) and inp_date[8:10] == "30":
        inp_date = inp_date[:5] + str(int(inp_date[5:7]) + 1) + "-01"
    if (inp_date[5:7] in ["01", "03", "05", "07", "08", "10"]) and inp_date[8:10] == "31":
        inp_date = inp_date[:5] + str(int(inp_date[5:7]) + 1) + "-01"
    else:
        dag = int(inp_date[8:10])
        dag += 1
        inp_date = inp_date[:8] + str(dag)
    return inp_date

print(is_input_valid(inp_date))