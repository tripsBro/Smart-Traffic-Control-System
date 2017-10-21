# Smart-Traffic-Control-System (work-on-progress)

Control System project on Smart Traffic. The pupose is to automate the traffic light which weighs in not only time but the number of cars on a lane.

**ALGORITHM**:

1. detect cars in the frame. Do this for all lanes.
2. count number of cars and label them with respect to their lane.
3. create a clock to count time and set a reference time for the command change.
4. in the reference time check and compare the number of cars in the present lane and next lane.
5. if the difference is more than 5 cars then initiate the change command.
