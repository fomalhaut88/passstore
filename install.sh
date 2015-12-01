if [ -d "dist" ]; then
    sudo cp dist/passstore /usr/bin;
    echo "installed successfully";
else
    echo "the program is not packed"
fi
