mod = ctrl + b

# get help
    ?

# open command
    :


# windows

## create window
    c

## rename window
    ,

## switch window
    p  -> prev window
    n  -> next window

## list window
    w



# pane (split)

## vertical split
    %

## horizontal split
    "

## 


# session

## create new sesstion
    tmux new-seesion -s mysesstion

## detach sesstion
    d 

## list all sessions
    tmux list-sessions

## reattach session
    tmux attach -t mysesstion
    
## kill session
    tmux kill-session -t mysesstion

## kill server (kill all session)
    tmux kill-server

    

## enable mouse
    set -g mouse on
