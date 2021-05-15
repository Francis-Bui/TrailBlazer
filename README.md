⛰️ TrailBlazer 🔥

The 2021 TurnerHacks project, TrailBlazar. Efficient extra-terrestrial path generation based off of topographic maps.

Built in under 24 hours, the software takes in two sets of coordinates, asks for a scale, and finds the most efficient path between the two.

![alt text](https://github.com/Francis-Bui/TurnerHacks-TrailBlazer/blob/master/GUI.png?raw=true)

GUI

![alt text](https://github.com/Francis-Bui/TurnerHacks-TrailBlazer/blob/master/pathDemo.png?raw=true)

Generated Path


Methedology:

The image representing the topographic map of the desired location is first scanned. From this scanning, we are able to access each pixel’s RGB values. 
Now, by convention, the color red represents high elevation. Thus, we’ve implemented a preferential system that gives maximum preference to the color red. 
Multiplying the red by the greatest value and then green value and then the blue value ends up in the red value accounting for most of the index that we have 
calculated, i.e. red has the most effect on the overall achieved index value. After red, naturally, green has the greatest value and this is again by the order
of increasing heights that is ordained by the conventions on such topographic representations of land. 

When we completed constructing the topological map, we then calculated the shortest path between two points in it. We used a version of the A-star 
algorithm to find the shortest path having visualized heights through the implementation of topographic graphical maps implemented into a 2D array. 

The A-Star algorithm is an informed version of Djikstras which uses a different method of ordering nodes. At each iteration rather than taking the node with the 
least distance from the origin node which is denoted by g, we take the node with the smallest f-value. The f-value is the sum of both the distance from the 
starting node and a heuristic calculated with respect to the final node. This ensures that the algorithm will favour nodes that are moving towards the destination 
point which increases efficiency as compared to Djikstras. 

The specific implementation details are as follows. We implemented the open set using a heap queue which keeps the nodes ordered in log(n) time. 
This results in a worst case time complexity of log(n) which is important for larger maps. The heuristic we used is consistent, or that is it ensures that the f-values are 
increasing for each added node. This is as a result of the heuristic guaranteeing an underestimation of the distance remaining to the destination node. 
It is easy to prove just by drawing a triangle. A consistent heuristic ensures that we are not revisiting any nodes twice with a better g value. This also means that it is g
uaranteed to find the shortest path in the end.

Finally, after the execution of the algorithm, Through data visualization techniques involving numpy and matplotlib libraries, we are able to show exactly what 
path the rover must take in an additional window.

