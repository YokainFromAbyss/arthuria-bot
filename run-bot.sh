while true
do
  python main.py &
  LAST_PID=$!

  read -r interrupt
  if [ "$interrupt" == "reboot" ]
  then
    echo "Reboot bot"
    kill $LAST_PID
  fi
  if [ "$interrupt" == "exit" ]
  then
    echo "Stopping bot"
    kill $LAST_PID
    exit 0
  fi
done