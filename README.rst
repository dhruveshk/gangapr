Installation and Using Ganga
------------
Installed ganga using the command

.. code-block:: bash

    pip install ganga

Use the command ganga to start ganga ipython prompt and create default .gangarc file.
python version used is 2.7.15

Splitting PDF
------------
The splpdf.py contains code to split the CERN.pdf file into individual pages script files.
It uses `PyPDF2`_ module to read the pdf and then output single pages files with the name cern[pgno].pdf eg: cern1.pdf has page number 1.

.. _PyPDF2: https://github.com/mstamy2/PyPDF2
Creating Job to count occurences
--------------------------------
rjob.py script first splits the pdf file and then creates a ganga job and submits it.

.. code-block:: python
    
      j = Job(splitter=s)
      j.outputfiles = ['tryout.txt']
      j.application.exe = File('try.py')
      j.merger = pm
      j.postprocessors.append(pm)
      j.submit()

Application property is set to try.py executable python file. 
The output of ganga job will be tryout.txt file. Custom Merger is add to postprocessor.
ArgumentSplitter uses the args attribute which is passed a list of the pdf files and creates multiple subjobs.
Each subjob reads the pdf file passed to it in the argument using `pdfminer`_ command line tool

.. _pdfminer: https://github.com/pdfminer/pdfminer.six

.. code-block:: bash

      pdf2txt.py cern1.pdf
      
, counts the occurence of the word "the" using 

.. code-block:: python

        c = string.count("the")

and outputs the result to tryout.txt file.


Custom Merger
------------------
CustomMerger class is passed the pdfmerger.py script. The script contains ``mergefiles(file_list,output_file)`` function which reads all the files in ``file_list`` adds the occurences and writes the output to ``output_file`` (tryout.txt)

Run and checking the output
-----------
Type in ganga ipython

.. code-block:: bash

    ganga rjob.py
    j.peek('tryout.txt')
    #for viewing subjob output
    j.subjobs(0).peek('tryout.txt')
 
 The output will be 313
 
Container
---------
The docker container is uploaded to dockerhub `here`_

.. _here: https://hub.docker.com/r/dhruveshk/dproj

The Dockerfile is uploaded to github.
To run the docker file type

.. code-block:: bash

    docker run -i -t dhruveshk/dproj:ganga

The container will execute the above ganga job and produce the output.
To view the output use

.. code-block:: bash

    !cat /root/gangadir/workspace/root/LocalXML/0/output/tryout.txt

Ganga Job for running container
--------------------------------
Installed docker for python using ``pip``

.. code-block:: bash

    pip install ganga
    
dockerex.py script runs the container.

.. code-block:: bash
      j = Job()
      j.application.exe = File('dockerex.py')
      j.submit()
      j.peek('stdout')

This creates a ganga job with executable file given as dockerex.py python script. It will run the container and ouput to stdout.
