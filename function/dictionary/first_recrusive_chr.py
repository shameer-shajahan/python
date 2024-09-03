

text="SCADDaA"

rpt_text={}

for l in text:

    if l in rpt_text:

        print(l)

        break

    else:

        rpt_text[l]=1
    