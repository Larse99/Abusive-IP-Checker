APP_NAME="Abusive-IP-Checker"
INSTALL_DIR="/opt/${APP_NAME}"
EXECUTABLE_NAME="ipcheck"
BIN_DIR="/usr/local/bin"

# Colors
GREEN="\033[0;32m"
RESET="\033[0m"

# Create installation directory
echo "Creating install directory at $INSTALL_DIR..."
sudo mkdir -p "$INSTALL_DIR"

# Copy the files to the installation directory
echo "Copying application files to $INSTALL_DIR..."
sudo cp -r includes scan.py "$INSTALL_DIR"

# Make executable
echo "Making the Python script executable..."
sudo chmod +x "$INSTALL_DIR/scan.py"

# Set permissions on includes directory
echo 'Fixing permissions'
sudo chmod -R 0755 "$INSTALL_DIR/includes"

# Create symlink to /usr/local/bin
echo "Creating symlink in $BIN_DIR..."
sudo ln -sf "$INSTALL_DIR/scan.py" "$BIN_DIR/$EXECUTABLE_NAME"

# Verify installation
if [ -x "$BIN_DIR/$EXECUTABLE_NAME" ]; then
    echo -e "${GREEN}Installation successful! You can now use '${EXECUTABLE_NAME}' from anywhere.${RESET}"
    echo -e "${GREEN}Don't forget to add your AbuseIPDB API key to ${INSTALL_DIR}/scan.py, in order to check IPs!"
else
    echo "Installation failed. Please check for errors."
    exit 1
fi

