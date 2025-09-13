Pyker Class Diagram
==================

.. mermaid::

    classDiagram
        Player "1" --> "1" Hand
        Player "1" --> "1" Wallet
        Table "1" --> "*" Player
        Dealer --|> Player
        Deck "1" --> "*" Card