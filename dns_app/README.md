Running on a Windows computer:
1. Open 4 Command Prompts
2. Ensure flask is installed on Python (pip install flask).
3. Start up the authoritative, fibonacci and user server using the command 'python fileName.py' using three Command Prompts.
4. In the fourth Command Prompt, make the Fibonacci server register with the authoritative server by running `curl -X PUT -H "Content-Type: application/json" -d "{\"hostname\":\"fibonacci.com\", \"ip\":\"IP NAME\", \"as_ip\":\"127.0.0.1\", \"as_port\":53533}" http://127.0.0.1:9090/register`
Replace the ip field in the JSON with the actual IP returned by the Flask application when the fibonacci server gets started. For example:

```
C:\NYU HW\DCN\Labs\Lab 3 Code>python fibonacciServer.py
 * Serving Flask app 'fibonacciServer'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:9090
 * Running on http://192.168.1.163:9090
```

In this case, the IP name is 192.168.1.163 or 127.0.0.1.

5. Once you see registration success, head to a browser (or use curl) to access the URL: http://127.0.0.1:8080/fibonacci?hostname=fibonacci.com&fs_port=9090&number=20&as_ip=127.0.0.1&as_port=53533
Change the number field to anything to see other results.

Alternatively, if you're running a Windows, use the .bat files provided. Make sure to run the start* files first before running the autoRegister.bat file.

If you re-run the program and registration fails, make sure that the dnsFile.txt is deleted so it can register again (if you want to re-register). If not, just rerun the program without re-registering.
