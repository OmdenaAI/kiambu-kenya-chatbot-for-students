class Util:
    """This class acts as source for creating helper functions consumed by the chat application.
    """

    @classmethod
    def incoming_event_callback(self) -> str:
        """This callback is  triggered when incoming messages arrive.
        """ 
        print("Incoming data")

        # TODO: Complete the implemtatation

        return ''

    @classmethod
    def process_input(self, message):
        #load the model pickle file and make a prediction for a user input
        res = f"You asked <strong>'{message}'</strong>. We will transfer you to availbe client to help out."
        return res
