import requests 
import json
from pathlib import Path 


def load_fav():
	try:	
		dis=1
		with open("favourites.json")as file:
			data=json.load(file)
		for i in data:
			print("name:",i["name"])
			print("launch data:",i["launch date"])
			print("lauch status:",i["launch status"])
			print("rocket name:",i["rocket name"])
			print("launch service provider:",i["launch service provider"])
			print("launch site:",i["launch site"])
			print("discription",i["discription"])
			print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
			dis+=1
		print("total displayed:",dis)
	except json.JSONDecodeError:
        	print("The JSON file is corrupted or improperly formatted.")
	

def get_fav(info):
	try:
		file_path=Path("favourites.json")
		new=info
		if file_path.exists():
			if file_path.stat().st_size==0:
				with open("favourites.json","w")as file:
					json.dump(new,file,indent=4)
				print("\n data saved successfully \n")
			else:
				if file_path.exists():
					with open(file_path,"r")as file:
						old=json.load(file)
				else:
					old=[]
		
				exists_data={
				i["name"] for i in old
				}
		
				if new["name"] not in exists_data:
					old.append(new)
					exists_data.add(new["name"])
				else:
					print("the data is save already ")
	
				with open("favourites.json","w")as file:
					json.dump(old,file,indent=4)
				print("\nsaved successfully \n")
	except FileNotFoundError:
		print("file not found ")								
						
	except json.JSONDecodeError:
        	print("The JSON file is corrupted or improperly formatted.")
        	

def view(name):
	try:
		url="https://lldev.thespacedevs.com/2.3.0/launches/upcoming/"
		response=requests.get(url,params={"search":name,"limit":100},timeout=10)
		print("json sataus code:",response.status_code)
		print()
		data=response.json()
		launchs=data["results"]
		if launchs:
			
			for launch in launchs:
				name=launch["name"]
				date=launch["net"]
				status=launch["status"]["name"]
				rocket=launch["rocket"]["configuration"]["name"]
				provider=launch["launch_service_provider"]["name"]
				launch_site=launch["pad"]["name"]
				description="no discription found about rocket"
				if launch["mission"]is not None:
					if launch["mission"]["description"] is not None:
						description=launch["mission"]["description"]
		
					
				original_url="original url not found"
				if len(launch["mission"]["agencies"])!=0:
					if len(launch["mission"]["agencies"][0]["info_url"])!=0:
						original_url=launch["mission"]["agencies"][0]["info_url"]
			
					youtube="youtube url is not found"
					if launch["mission"]["agencies"][0]["social_media_links"]:
						yurl=launch["mission"]["agencies"][0]["social_media_links"]
						for i in yurl:
							if i["social_media"]["name"] == "Youtube":
								youtube=i["url"]
				else:
					youtube="youtube url is not found"
					original_url="original url not found"
				print(f"name:{name}")
				print(f"launch date:{date}")
				print(f"launch status:{status}")	
				print(f"rocket name:{rocket}")
				print(f"launch service provider:{provider}")
				print(f"launch site:{launch_site}")
				print(f"description:{description}")
				print(f"offical url:{original_url}")
				print(f"youtube url:{youtube}")
				print("============================================")
	except requests.exceptions.Timeout:
	   	print("Request timed out. Please try again.")
	except requests.exceptions.ConnectionError:
	   	print("No internet connection.")
	except requests.exceptions.RequestException:
	   	print("There was a problem with the API request.")
	except (KeyError, TypeError):
	  	 print("please enter year-month-day correctle")

def filter(start,end):
	try:
		url="https://lldev.thespacedevs.com/2.3.0/launches/upcoming/"
		response=requests.get(url,params={"net__gte":start,"net__lte":end,"limit":100},timeout=10)
		print("json sataus code:",response.status_code)
		print()
		data=response.json()
		launchs=data["results"]
		count=1
		if launchs:
			for launch in launchs:
				name=launch["name"]
				date=launch["net"]
				status=launch["status"]["name"]
				rocket=launch["rocket"]["configuration"]["name"]
				provider=launch["launch_service_provider"]["name"]
				launch_site=launch["pad"]["name"]
				description="no discription found about rocket"
				if launch["mission"]is not None:
					if launch["mission"]["description"] is not None:
						discription=launch["mission"]["description"]
		
				print(count)
				print(f"name:{name}")
				print(f"launch date:{date}")
				print(f"launch status:{status}")	
				print(f"rocket name:{rocket}")
				print(f"launch service provider:{provider}")
				print(f"launch site:{launch_site}")
				print(f"discription:{discription}")
				print("============================================")
				count+=1
		else:
			print("not found ")
	except requests.exceptions.Timeout:
	   	print("Request timed out. Please try again.")
	except requests.exceptions.ConnectionError:
	   	print("No internet connection.")
	except requests.exceptions.RequestException:
	   	print("There was a problem with the API request.")
	except (KeyError, TypeError):
	  	 print("please enter year-month-day correctle")


def search(name):
	try:
		url="https://lldev.thespacedevs.com/2.3.0/launches/upcoming/"
		response=requests.get(url,params={"search":name,"limit":100},timeout=10)
		print("json sataus code:",response.status_code)
		data=response.json()
		launchs=data["results"]
		found=0
		if launchs:
			for launch in launchs:
				name=launch["name"]
				date=launch["net"]
				status=launch["status"]["name"]
				rocket=launch["rocket"]["configuration"]["name"]
				provider=launch["launch_service_provider"]["name"]
				launch_site=launch["pad"]["name"]
				description="no discription found about rocket"
				if launch["mission"]is not None:
					if launch["mission"]["description"] is not None:
						discription=launch["mission"]["description"]
		
		
				print(f"name:{name}")
				print(f"launch date:{date}")
				print(f"launch status:{status}")	
				print(f"rocket name:{rocket}")
				print(f"launch service provider:{provider}")
				print(f"launch site:{launch_site}")
				print(f"discription:{discription}")
				print("============================================")
				found+=1
			print("total found:",found)
		else:
			print("not found ")
	except requests.exceptions.Timeout:
	   	print("Request timed out. Please try again.")
	except requests.exceptions.ConnectionError:
	   	print("No internet connection.")
	except requests.exceptions.RequestException:
	   	print("There was a problem with the API request.")
	except (KeyError, TypeError):
	  	 print("Unexpected data received from the API.")
	
		

def display():
	try:
		url="https://lldev.thespacedevs.com/2.3.0/launches/upcoming/"
		response=requests.get(url,params={"limit":100},timeout=10)
		print("json sataus code:",response.status_code)
		print()
		data=response.json()
		launchs=data["results"]
		count=1
		space_data=[]
		for launch in launchs:
			name=launch["name"]
			date=launch["net"]
			status=launch["status"]["name"]
			rocket=launch["rocket"]["configuration"]["name"]
			provider=launch["launch_service_provider"]["name"]
			launch_site=launch["pad"]["name"]
			description="no discription found about rocket"
			if launch["mission"]is not None:
				if launch["mission"]["description"] is not None:
					discription=launch["mission"]["description"]
		
			print(count)
			print(f"name:{name}")
			print(f"launch date:{date}")
			print(f"launch status:{status}")	
			print(f"rocket name:{rocket}")
			print(f"launch service provider:{provider}")
			print(f"launch site:{launch_site}")
			print(f"discription:{discription}")
			print("============================================")
			count+=1
			space_list={"name":name,
			"launch date":date,
			"launch status":status,
			"rocket name":rocket,
			"launch service provider":provider,
			"launch site":launch_site,
			"discription":discription}
			space_data.append(space_list)
		return space_data
	except requests.exceptions.Timeout:
	   	print("Request timed out. Please try again.")
	except requests.exceptions.ConnectionError:
	   	print("No internet connection.")
	except requests.exceptions.RequestException:
	   	print("There was a problem with the API request.")
	except (KeyError, TypeError):
	  	 print("Unexpected data received from the API.")
def mane():
	try:
		space=[]
		while True:
			print("===== SPACE LAUNCH MENU =====")
			print("1. Display upcoming launches")
			print("2. Search launch by name")
			print("3. Filter launches by date")
			print("4. View launch details")
			print("5. Save a launch to favourites")
			print("6. Display saved favourites")
			print("7. Exit")
			a=int(input("Enter your choice:"))
			
			if a==7:
				break
			if a==1:
				result=display()
				if result is not None:
					space=result
			if a==2:
				name=input("enter name:")
				if not name.strip():
					print("name can be empty")
				else:
					search(name)
			if a==3:
				
				start=input("enter start date:")
				end=input("enter end date:")
				if not start.strip():
					print("start can't be empty ")
					if not end.strip():
						print("end can't be empty")
				else:
					filter(start,end)
			if a==4:
				try:			
					print()
					for i,j in enumerate(space,start=1):
						print(i,".",j["name"])
					choice=int(input("enter your choice number:"))
					for i,j in enumerate(space,start=1):
						if i == choice:
							view(j["name"])
				except UnboundLocalError:
					print("please first use option 1 to get launch details\n")
			if a==5:
				try:
					print()
					for i,j in enumerate(space,start=1):
						print(i,".",j["name"])
					saved=0
					choose=int(input("enter number tonsave in favourite:"))
					for i,j in enumerate(space,start=1):
						if i==choose:
							get_fav(j)
							saved+=1
																	 												
					if saved==0:
						print("enter valid number")	
					
					
				except UnboundLocalError:
					print("please first use option 1 to load data to save in favourites\n")
			
			if a==6:
				load_fav()
	except ValueError:
			print("enter number not text")	
mane()	