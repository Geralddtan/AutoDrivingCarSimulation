# Auto Driving Car Simulation

## Design Considerations

In designing the OOP structure for the Auto Driving Car Simulation a few main considerations were made:

- I created separate classes for each object - Vehicle, Field, GridPoint, Collision to represent them as Objects as much as possible
- I wanted to ensure that circular dependency between Vehicle and field is not present. The situation of "Field HAS-A Vehicle and Vehicle HAS-A Field" should not occur. While such circular dependency is necessary in some situations, it is not ideal. As a result, I generated an additional class VehicleManager which serves as the central manager which links Vehicle and Field. A VehicleManager has cars and a field attached to it which it is in charge of. NAturally, this class performs the core function which moves vehicles around the field
- In order to make the solution extensible, I created Vehicle as an abstract base class with some base implementations. An AutoDrivingCar being a type of vehicle will then implement the Vehicle abstract class. For future extensions to the code for other vehicles, they simply need to implement the Vehicle abstract class just as how AutoDrivingCar does. The Vehicle Abstract Class has a function move() which is not implemented. This is because different vehicles could have different moving patterns.

## Assumptions

Several assumptions were made for both parts of the question and these assumptions were made based on the logical flow of events

1. Each vehicle must be initialised with at least 1 command and commands must strictly be "F", "L", "R"
2. Each vehicle can have different length of commands
3. Vehicles CANNOT be initialised outside of the field boundary
4. If collisions occur, the collision is shown and the method ends (no future collision will be shown even if it is present)
5. If multiple separate collisions happen at the same time, all collisions will be shown
6. All vehicles involved in collision will be shown (Can be more than 2 vehicles involved in a collision)
7. If 2 vehicles pass by each other, no collision will occur. If Car A is at 1 1 N going Forward, and Car B is at (1 2 S) going Forward, no collision will occur
8. 2 Vehicles initialised at the same starting point is not considered a crash. As per the question, a crash only occurs when 2 vehicles want to move to the same point.

## Instructions to Run Code

- Environment used to run: MacOS

Part 1:
In order to run Part 1, simply run the following commands:

```
python main_part1.py
```

After running the above command, you will be prompted to input an input text file name. For example:

```
./input.txt
```

These above steps will run the part 1 code and output the desired response

Part 2:
In order to run Part 2, simply run the following commands:

```
python main_part2.py
```

After running the above command, you will be prompted to input an input text file name. For example:

```
./input2.txt
```

These above steps will run the part 2 code and output the desired response

## Testing

In order to run the provided pytest cases, you can run the following command:

```
python -m pytest test/
```
