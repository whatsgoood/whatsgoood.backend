# WhatsGoood backend Project

This repo serves as the backend(REST API) repo for the WhatsGoood web application. 

## Description

The main component of the backend is a python-flask rest Api service.
Json data can be retrieved from a cloud mongodb, which is then processed to output ratings for a list of supported 
sports. Ratings are generated by applying preconfigured sport-specific weights to live or forecasted weather data. 

## Getting Started

### Installing

* Clone the repo
* Create an environment
   1. You need two environment vars
        * `WHATSGOOOD_ENV` - set to one of these two:
            * config.DevelopmentConfig
            * config.ProductionConfig
        * `WHATSGOOOD_CONSTR` - connection string to the mongodb
          * You'll need to get this from the owners
   2. Install requirements:
        ```
        pip install -r requirements.txt
        ```
### Executing program

Running locally:

```
python run.py
```

### Contributing:

#### Development:
* Follow git-flow
    * feat/
    * change/
    * defect/
1. Branch develop
2. commit changes to feature branch
3. PR to develop
4. PR develop to master 

#### Deployments :
* There are dev and production servers on heroku
* Request to become a colloborator on the heroku projects to get a git remote url
    * To deploy feature branches to dev server
        1. Add the heroku dev repo as a remote in git
        2. Push to dev server:
            ```
            git push <remoteUrlName> <yourFeatureBranchName>:master
            ```
    *  Deploy to prod:
        1. Add the heroku prod repo as a remote in git
        1. Push to prod server:
            ```
            git push <remoteUrlName> master
            ```


## Authors

Rob Kritzinger - [@Zingers-ZA](https://github.com/Zingers-ZA)  
Dylan Graham - [@Dylan-Graham](https://github.com/Dylan-Graham)  
