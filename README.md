Joel Ejchental
Home Assignment

Explanation:
As I mentioned to Josh, I had some difficulties completing the assignment for a laptop camera using a ubuntu image because I’m using a MAC. I spoke to Josh and he advised me that I can use any external hardware device. Thus, I decided to create one. I used an Arduino and connected 2 devices; an ultrasonic sensor that measures distance by sound waves and a fan motor (photo below). I had to add a pull down 10[Kohm] resistor on the fan motor connection to accurately control it remotely. I wrote an Arduino sketch to the Arduino for basic commands to control the sensor and fan. 
I had many issues on my mac passing the Hardware device to docker using docker-ce and docker desktop so I used a virtual machine (UTM) and created the automation framework in a docker and scripted the tests with an interactive python script based on a serial port connection. Of course there is a log that tracks the test. Once finished, I scp’d the directory to my MAC and will attach it to the email. Within the directory is /logs/hw_test.log which already contains some small tests I ran to show basic functionality. 
Of course, the script itself can be much more robust, and more edge cases need to be added, but at this point I think I demonstrated my abilities clearly. Furthermore, I will add that until now I’ve had very little experience with virtual machines, dockers, and Arduino but I found the assignment very interesting, so I used this opportunity to learn.
As you don’t have the device, you won’t be able to run it, but if you did the 2 commands would be:
1.)	docker build -t hw_testing .
2.)	docker run –-rm -it –-privileged –-device=/dev/ttyACM0 -v $(pwd)/logs:app/logs hw_testing
![image](https://github.com/user-attachments/assets/6dc4b402-4c7f-4121-9935-9f163e6b3511)
