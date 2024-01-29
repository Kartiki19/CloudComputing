# Download Docker
https://docs.docker.com/desktop/install/mac-install/

# Check Docker Version<br>
```docker --version```

<br>![image](https://github.com/Kartiki19/CloudComputing/assets/120880459/d92e770e-f897-46f5-9944-af8182c9449e)

# Docker for Ubuntu 20.04 OS
```docker pull ubuntu:20.04```

# List all the locally available images
```docker image ls```

<br><img width="790" alt="image" src="https://github.com/Kartiki19/CloudComputing/assets/120880459/4614bb34-fa11-4ed7-958b-1cf34fea94cf">


# Run an image with interactive bash shell inside the container
```docker run -it ubuntu:20.04 /bin/bash```

# Create a Dockerfile
Creating customized docker image with Ubuntu 20.04 and SysBench:

<br><img width="448" alt="image" src="https://github.com/Kartiki19/CloudComputing/assets/120880459/bbb7e3cc-e2d2-4be5-ad3a-d04cedbbefd9">

# Build Docker ubuntu + sysbench image
1. Use following command to build the image using the Dockerfile mentioned above.
2. Place the Docker file in the current working directory OR
3. Replace '.' with the folder location of the Dockerfile
4. ubuntusysbench = name of the image | 1.0 = tag for the image <br><br>

  ```docker build -t ubuntusysbench:1.0 .```

# Run container and check sysbench version
2. To get the version of sysbench running, add --version while running the container <br><br>
```docker run --rm ubuntusysbench:1.0 --version```

<br><img width="1111" alt="image" src="https://github.com/Kartiki19/CloudComputing/assets/120880459/54369613-288d-440b-9c61-98674b9317f2">

# Capture image ID
```docker images | grep ubuntusysbench```

# Check image history
<br>```docker history <image_id>```

<img width="807" alt="image" src="https://github.com/Kartiki19/CloudComputing/assets/120880459/19b95bfc-33e0-4feb-9565-dc5d91a3a7ea">

<br> <br> Save the history in a 'image_history.txt'

<br>```docker history <image_id> > image_history.txt```

<br><img width="1325" alt="image" src="https://github.com/Kartiki19/CloudComputing/assets/120880459/8eb26f66-c953-4b47-a357-0aa6285fdf63">

