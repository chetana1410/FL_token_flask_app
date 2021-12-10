from brownie import FELToken, ProjectContract, accounts, config, network
from scripts.helpful_scripts import (
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
    fund_with_link,
    get_account,
    get_contract,
)
from sklearn.linear_model import LinearRegression 
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor


from felt.builder import upload_model

def user_inputs(form):
    
    model_type = form["model"]
    rounds = int(form["rounds"])
    tokens = int(form["tokens"])
    address = form["address"]
    
    
    project = ProjectContract[-1]
    builder = accounts.add(config["wallets"]["owner_key"])

    
   
    fund_with_link(address)

    ## DEFINE MODEL ###
    if model_type=='linear':
        model = LinearRegression()
    elif model_type=='svm': 
        model = SVR(kernel=form(["kernel"]))
    elif model_type=='random forest':
        model = RandomForestRegressor()
        
    cid = upload_model(model)
    
    return cid
   

    # ### PROVIDE REWARDS AND UPLOAD PLAN ###
    # FELToken[-1].increaseAllowance(address, 1000, {"from": builder})
    # requestId = project.createPlan(cid, rounds, tokens, {"from": builder})

    # # Simulate the VRF on local chain
    # if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
    #     get_contract("vrf_coordinator").callBackWithRandomness(
    #         requestId.return_value, 777, address, {"from": get_account()}
    #     )
        


        

        


