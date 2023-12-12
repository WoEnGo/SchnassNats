# SchnassNats Probability Library

## Overview
The SchnassNats Probability Library is a simple Python class that facilitates the management of events and their associated probabilities. This library is particularly useful for scenarios where you need to model and work with events that have distinct likelihoods.

## Features
**Add Events:** Easily add events along with their corresponding probabilities to the library.
**Remove Events:** Remove events from the library that are no longer relevant.
**Get Event Probability:** Retrieve the probability of a specific event.
**Get All Events:** Obtain a list of all events currently in the library.
**Get Total Probability:** Calculate the total probability of all events in the library.
**Pick Random Event:** Randomly select an event based on their assigned probabilities.

## Getting Started
**Installation:** Simply copy the `SchnassNats` class into your Python project.
**Initialization:**
```py
schnass_nats = SchnassNats()
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
# Create an instance of SchnassNats
probability_library = SchnassNats()

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
The library ensures that probabilities are within the valid range of 0 to 100.
Removing an event that does not exist in the library will raise a `ValueError`.
Attempting to access the probability of a nonexistent event will also raise a `ValueError`.

Feel free to use this library to model and simulate scenarios involving uncertain events and their likelihoods. If you encounter any issues or have suggestions for improvements, please open an issue or contribute to the project. Happy coding!

Communications for Discord.
Discord my nickname: MVXXL
