import capsolver
from urllib.parse import urlparse

# Change this information
capsolver.api_key = "Your pay per usage key"

def solve_recaptcha_v3_enterprise():
    solution = capsolver.solve({
      "type": "ReCaptchaV3EnterpriseTaskProxyless",
        "websiteURL": "https://www.netflix.com",
        "websiteKey": "6Lf8hrcUAAAAAIpQAFW2VFjtiYnThOjZOA5xvLyR",
        "pageAction": "login"
    })
    return solution

def main():
    
    print("Solving netflix captcha")
    solution = solve_recaptcha_v3_enterprise()
    
    token = solution["gRecaptchaResponse"]
    
    print("Token Solution " + token)
    
if __name__ == "__main__":
    main()
