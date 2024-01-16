# SchnassNats Probability Library V2

## Overview
The SchnassNats Probability Library (Version 2) is an enhanced Python class designed to streamline the management of events and their associated probabilities. This library is particularly useful for scenarios where modeling events with distinct likelihoods is essential.

## Features
**Add Events:** Easily add events along with their corresponding probabilities to the collection.
**Remove Events:** Remove events from the collection that are no longer relevant.
**Get Event Probability:** Retrieve the probability of a specific event.
**Get All Events:** Obtain a list of all events currently in the collection.
**Get Total Probability:** Calculate the total probability of all events in the collection.
**Pick Random Event:** Randomly select an event based on their assigned probabilities.
**Get High Probability Events:** Retrieve events with probabilities higher than a specified threshold.
**Get Low Probability Events:** Retrieve events with probabilities lower than a specified threshold.
**Update Event Probability:** Modify the probability of a specific event.
**Get Most Probable Event:** Retrieve the event with the highest probability.
**Get Least Probable Event:** Retrieve the event with the lowest probability.
**Clear All Events:** Remove all events from the collection.
**Get Average Probability:** Calculate and return the average probability of all events.
**Get Randomized Event Order:** Return a list of events in a randomized order.
**Scale Probabilities:** Scale all event probabilities by a given factor.


## Getting Started
**Installation:** Simply copy the `SchnassNats` class into your Python project.
**Initialization:**
```py
probability_library = SchnassNats()
```
**Adding Events:**
```py
schnass_nats.add_event("Event1", 30)
schnass_nats.add_event("Event2", 20)
```
**Removing Events:**
```py
schnass_nats.remove_event("Event1")
```
**Getting Event Probability:**
```py
probability = schnass_nats.get_event_probability("Event2")
```
**Getting All Events:**
```py
events = schnass_nats.get_all_events()
```
**Getting Total Probability:**
```py
total_probability = schnass_nats.get_total_probability()
```
**Picking Random Event:**
```py
random_event = schnass_nats.pick_random_event()
```
# Example Usage
```py
# Add events with their probabilities
probability_library.add_event("High", 70)
probability_library.add_event("Medium", 20)
probability_library.add_event("Low", 10)

# Get total probability
total_prob = probability_library.get_total_probability()

# Pick a random event based on probabilities
random_event = probability_library.pick_random_event()
```
# Error Handling
The library ensures that probabilities are within the valid range of 0 to 100. Removing an event that does not exist in the collection will raise a ValueError. Attempting to access the probability of a nonexistent event will also raise a ValueError.

# Difference from Version 1
The SchnassNats Probability Library (Version 2) introduces several new features, including the ability to:

• Retrieve events with probabilities higher or lower than a specified threshold.
• Update the probability of a specific event.
• Get the most and least probable events.
• Clear all events from the collection.
• Calculate the average probability of all events.
• Get events in a randomized order.
• Scale all event probabilities by a given factor.

Feel free to utilize this library to model and simulate scenarios involving uncertain events and their likelihoods. If you encounter any issues or have suggestions for improvements, please open an issue or contribute to the project. Happy coding!

Communications for Discord.
Discord my nickname: MVXXL
