import os
def mergefiles(file_list,output_file):
      counter = 0
      with open('ka.txt','w') as jp:
          jp.write(output_file)
      f_out = file(output_file,'w')
      for f in file_list:
            f_in = file(f)
            counter = int(f_in.read())+counter
            f_in.close()
      f_out.write(str(counter))
      f_out.flush()
      f_out.close()
      return True
