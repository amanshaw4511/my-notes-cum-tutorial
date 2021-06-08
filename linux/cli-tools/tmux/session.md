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

## swithc session
    (   -> next session
    )   -> prev session


## kill server (kill all session)
    tmux kill-server

