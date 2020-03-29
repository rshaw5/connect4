# Introduction
Ever since I learned of it, I have been enamored with the TDD concept. In an effort to expand my knowledge of both Python and AI, I am attempting to work through the following two tutorials while modifying them to fit the TDD process:

- [Connect Four Game](https://www.youtube.com/watch?v=XpYz-q1lxu8)
- [Connect Four AI](https://www.youtube.com/watch?v=8392NJjj8s0)

A comment on my styling: in general, I am interested in self-documenting and readable code over optimization or fancy tricks to reduce lines.

I also value vertical alignment when it adds readability to code. User [matthewthorning](https://marketplace.visualstudio.com/publishers/matthewthorning) created an [excellent vertical alignment tool for VS Code](https://marketplace.visualstudio.com/items?itemName=matthewthorning.align-vertically). I take advantage of this tool whenever it makes sense.

I find comments that precede code to be distracting, they break my flow while reviewing. To combat this, I use "footnotes" and "endnotes". Footnotes follow the end of a logical block, while endnotes appear after the end of the current scope. For example:

```python
self.assertEqual(actualArrayMetadata        , expectedArrayMetadata)    # Footnote 1
self.assertEqual(gameVariables.gameOver     , False)
self.assertEqual(gameVariables.turnNumber   , 1)
self.assertEqual(gameVariables.currentPlayer, 1)

# FOOTNOTES:
#   1. This duplicates test_setup_game_board. Is it possible to reuse any code?
```

This helps me keep my flow while reading code, as well as place long comments on specific lines without making a mess. Footnote numbering restarts after each logical block, endnote numbers restart after the end of each scope. This helps keep numbering straight if major changes are made to code, since I don't have a programatic way to add them (yet).

As always, my goal is to write clear, maintainable, useful code for myself and others. Comments and insights are always appreciated!

# Concepts Learned
Here I will log the concepts I learned during this process. This log is for both myself and anyone coming by later that may be interested in my thought process.

## Redirecting stdout
We need a way to examine stdout in order to test a function like this:

```python
print(f"Player {player}, make your selection (1-7):")
```

[This Stackoverflow thread](https://stackoverflow.com/questions/4219717/how-to-assert-output-with-nosetest-unittest-in-python/31281467) gave me some insight into the process. I was able to determine that, for my purposes, the following code is sufficient:

```python
with patch('sys.stdout', new=StringIO()) as fakeOutput:
    connect4.prompt_player(1)
    self.assertEqual(fakeOutput.getvalue().strip(), expectedValue)
```

### TODO
- What is the ```with``` command and how is it used?
- What is the ```patch``` command and how it is used?
- What is the line ```new=StringIO())``` doing?
- Understand how ```fakeOutput``` is formatted and how ```getvalue()``` and ```strip()``` interact with it.

------

## assertRaises
One of the tests needs to ensure that the game exits properly. To exit, the game calls this code:

```python
if gameVariables.gameOver:
    sys.exit(0)
```

For a while, I wasn't sure if I could test this behavior; but [this Stackoverflow thread](https://stackoverflow.com/questions/15672151/is-it-possible-for-a-unit-test-to-assert-that-a-method-calls-sys-exit) helped me nail down the following test:

```python
with self.assertRaises(SystemExit):
    connect4.game_loop_step(gameVariables)
```

### TODO
- Understand the ```with``` command and how it's used

------