#!/bin/bash

SCRIPT=$(readlink -f $0)
SCRIPTPATH=`dirname $SCRIPT`

if [ $# -eq 0 ] || [ $1 = "-h" ] || [ $1 = "--help" ]; then
  echo "Usage:" 
  echo "deploy_unity_plugins.sh <PLUGINS_DIR>"
  echo ""
  echo "PLUGINS_DIR - Ros2ForUnity/Plugins folder."
  exit 1
fi

pluginDir=$1

mkdir -p  ${pluginDir}/Android/
find install/lib/dotnet/ -maxdepth 1 -not -name "*.pdb" -type f -exec cp {} ${pluginDir} \;
cp $SCRIPTPATH/install/standalone/* ${pluginDir}/Android/ 2>/dev/null
find install/lib/ -maxdepth 1 -not -name "*_python.so" -type f -exec cp {} ${pluginDir}/Android/ \;
cp $SCRIPTPATH/install/resources/*.so ${pluginDir}/Android/ 2>/dev/null
