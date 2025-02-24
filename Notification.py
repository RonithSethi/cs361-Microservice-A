from time import sleep

count = 0 # Current second
amount = 0 # Total time to wait before notifying
x = 0 # Placeholder for the string in pipeA.txt
while True:
    sleep(1)
    with open("pipeA.txt", "r") as prng:
        x = prng.read()

    # Executes when a new integer is written
    if x.isdigit():
        count = 0
        amount = int(x) * 60 # convert X (minutes) to seconds
        y = open("pipeA.txt", "w") # clear the txt file
        y.close()

    # Executes when 'cancel' is written
    if x == "cancel":
        count = 0 # reset variables
        amount = 0
        y = open("pipeA.txt", "w") # clear the txt file
        y.close()

    if amount != 0:
        count += 1

        # Executes when the full time has elapsed
        if count >= amount:
            y = open("pipeA.txt", "w")
            y.write("beep")
            # print("beep was written in the txt file.")
            # ^ test print ^
            y.close()
            amount = 0 # reset variables
            count = 0