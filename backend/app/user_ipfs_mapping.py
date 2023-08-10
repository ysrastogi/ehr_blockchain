from flask import Flask
import ipfshttpclient

app = Flask(__name__)

ipfs_client = ipfshttpclient.connect("")
user_ipfs_mapping = {}
