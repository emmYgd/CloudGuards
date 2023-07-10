'''
ask() ->
sends a message and waits for a response message (or a timeout). Note that the response message does not have to be from the same Actor that the input message was sent to, and the receipt of any message counts as a response.
tell() ->
queues a message for transmission to the indicated Actor and returns immediately. The message may or may not have been delivered to the target Actor by the time this call returns.
listen() ->
waits for a response message or a timeout.

ActorSystem API	Actor methods:
ask()
tell()
send()
listen()
receiveMessage() method invoked

Actor Architecture:
The outside (Rest of the program - Main) contacts the ActorSystem for specific implementation->
=> ActorSystem in implementation sends messages to the Coordinators
=> Coordinators send messages to the Factories for work.
=> Factories do work concurrently via Actor Troupe strategy and
Returns the results asynchronously to the Coordinators =>
Coordinators return work to the ActorSystem call =>
Yields control to the outside (Rest of the program - Main)
'''