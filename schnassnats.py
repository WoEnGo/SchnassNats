import random

class SchnassNats:
    def __init__(self):
        self.events = {}

    def add_event(self, event, probability):
        """
        Adds an event along with its probability to the collection.
        :param event: Event
        :param probability: Probability of the event (in percentage)
        """
        if not (0 <= probability <= 100):
            raise ValueError("Probability must be between 0 and 100")

        total_probability = self.calculate_total_probability()
        if total_probability + probability <= 100:
            self.events[event] = probability
        else:
            raise ValueError("Total probability cannot exceed 100%")

    def remove_event(self, event):
        """
        Removes an event from the collection.
        :param event: Event
        """
        if event in self.events:
            del self.events[event]
        else:
            raise ValueError(f"Event '{event}' not found in the collection")

    def get_event_probability(self, event):
        """
        Gets the probability of a specific event.
        :param event: Event
        :return: Probability of the event (in percentage)
        """
        return self.events.get(event, None)

    def get_all_events(self):
        """
        Gets a list of all events in the collection.
        :return: List of events
        """
        return list(self.events.keys())

    def calculate_total_probability(self):
        """
        Calculates the total probability of all events in the collection.
        :return: Total probability (in percentage)
        """
        return sum(self.events.values())

    def pick_random_event(self):
        """
        Picks a random event based on their probabilities.
        :return: Random event
        """
        if not self.events:
            raise ValueError("The collection is empty. Add events with their probabilities.")
        
        random_number = random.uniform(0, 100)
        cumulative_probability = 0

        for event, probability in self.events.items():
            cumulative_probability += probability
            if random_number <= cumulative_probability:
                return event

    def get_high_probability_events(self, threshold):
        """
        Gets a list of events with probabilities higher than the given threshold.
        :param threshold: Minimum probability threshold (in percentage)
        :return: List of events with probabilities higher than the threshold
        """
        return [event for event, probability in self.events.items() if probability > threshold]

    def get_low_probability_events(self, threshold):
        """
        Gets a list of events with probabilities lower than the given threshold.
        :param threshold: Maximum probability threshold (in percentage)
        :return: List of events with probabilities lower than the threshold
        """
        return [event for event, probability in self.events.items() if probability < threshold]

    def update_event_probability(self, event, new_probability):
        """
        Updates the probability of a specific event.
        :param event: Event
        :param new_probability: New probability of the event (in percentage)
        """
        if not (0 <= new_probability <= 100):
            raise ValueError("Probability must be between 0 and 100")

        if event in self.events:
            current_total_probability = self.calculate_total_probability() - self.events[event]
            if current_total_probability + new_probability <= 100:
                self.events[event] = new_probability
            else:
                raise ValueError("Total probability cannot exceed 100%")
        else:
            raise ValueError(f"Event '{event}' not found in the collection")

    def get_most_probable_event(self):
        """
        Gets the event with the highest probability.
        :return: Event with the highest probability
        """
        if not self.events:
            raise ValueError("The collection is empty. Add events with their probabilities.")
        
        return max(self.events, key=self.events.get)

    def get_least_probable_event(self):
        """
        Gets the event with the lowest probability.
        :return: Event with the lowest probability
        """
        if not self.events:
            raise ValueError("The collection is empty. Add events with their probabilities.")
        
        return min(self.events, key=self.events.get)

    def clear_all_events(self):
        """
        Clears all events from the collection.
        """
        self.events.clear()

    def get_average_probability(self):
        """
        Calculates and returns the average probability of all events.
        :return: Average probability (in percentage)
        """
        total_probability = self.calculate_total_probability()
        num_events = len(self.events)
        return total_probability / num_events if num_events > 0 else 0

    def get_randomized_event_order(self):
        """
        Returns a list of events in a randomized order.
        :return: List of events in a randomized order
        """
        randomized_order = list(self.events.keys())
        random.shuffle(randomized_order)
        return randomized_order

    def scale_probabilities(self, factor):
        """
        Scales all event probabilities by the given factor.
        :param factor: Scaling factor
        """
        if factor <= 0:
            raise ValueError("Scaling factor must be greater than 0")

        for event in self.events:
            self.events[event] *= factor
