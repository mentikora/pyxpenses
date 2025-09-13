Pyker Class Diagram
==================

.. mermaid::

    classDiagram
        Player --> Hand
        Player -> Wallet
        Table --> Player
        Dealer <|-- Player
        Deck --> Card