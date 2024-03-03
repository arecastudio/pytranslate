import sys
import translators as ts

result=''
# Next, run a simple conditonal statement to check if argv exists
if (len(sys.argv)) > 1:
    result = sys.argv[1]
else:
    result = False
# Finally, you can use the result from the above test and run further code accordingly
if result == False:
    print("argv DOES NOT exist!")
else:
  #print("argv exists!")
  if result!='':
      try:
        qtxt='ini hari apa'
        print(ts.translate_text(result))
      except Exception as err:
        print(err)

#q_text='hari ini makan apa'

#print(ts.translate_text(q_text))
