import random

class SchnassNats:
    def __init__(self):
        self.probabilities = {}

    def add_event(self, event, probability):
        """
        Adds an event and its probability to the library.
        :param event: Event
        :param probability: Probability of the event (in percentage)
        """
        if 0 <= probability <= 100:
            if self.get_total_probability() + probability <= 100:
                self.probabilities[event] = probability
            else:
                raise ValueError("Total probability cannot exceed 100%")
        else:
            raise ValueError("Probability must be between 0 and 100")

    def remove_event(self, event):
        """
        Removes an event from the library.
        :param event: Event
        """
        if event in self.probabilities:
            del self.probabilities[event]
        else:
            raise ValueError(f"Event '{event}' not found in the library")

    def get_event_probability(self, event):
        """
        Gets the probability of an event.
        :param event: Event
        :return: Probability of the event (in percentage)
        """
        if event in self.probabilities:
            return self.probabilities[event]
        else:
            raise ValueError(f"Event '{event}' not found in the library")

    def get_all_events(self):
        """
        Gets a list of all events in the library.
        :return: List of events
        """
        return list(self.probabilities.keys())

    def get_total_probability(self):
        """
        Gets the total probability of all events in the library.
        :return: Total probability (in percentage)
        """
        return sum(self.probabilities.values())

    def pick_random_event(self):
        """
        Picks a random event based on their probabilities.
        :return: Random event
        """
        if not self.probabilities:
            raise ValueError("The library is empty. Add events with their probabilities.")
        
        rand_num = random.uniform(0, 100)
        cumulative_prob = 0

        for event, probability in self.probabilities.items():
            cumulative_prob += probability
            if rand_num <= cumulative_prob:
                return event
