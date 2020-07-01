# **Guessing Game**

The script accepts 0, 1 or 2 command line arguments which define the range of numbers to guess from.

The following are valid ways to run the script:

1. The first form takes zero command line arguments and defaults to the built-in range 0 - 10.


    `python guess.py`



2. The second form takes 1 command line argument and uses the passed value as the upper limit. The example below assumes the range 0 - 20

     `python guess.py 20`

3. The third form takes 2 command line arguments. The first argument being the lower value and the second argument being the upper limit. 

    `python guess.py 0 100`

Any other form e.g. lower value larger than upper value `python guess.py 20 10` or more than 2 command line arguments being passed `python guess.py 0 10 20` will be invalid and the script defaults to the internal range 0 - 10.