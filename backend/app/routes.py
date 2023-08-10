from flask import request, jsonify
from app import app, ipfs_client, user_ipfs_mapping

@app.route('/register', methods=['POST'])
def register_patient():
    try:
        data = request.get_json()

        abha_id = data['abha_id']

        patient_data = {
            'name': data['name'],
            'age': data['age'],
            'gender': data['gender'],
            'aadhar_no': data['aadhar no.'],
            'abha_id': abha_id,
            'phone no.': data['phone_no']
                    
        }
        ipfs_hash = ipfs_client.add_json(patient_data)

        user_ipfs_mapping[abha_id] = ipfs_hash
        return jsonify({'ipfs_hash': ipfs_hash})
    except Exception as e:
        return jsonify({'error': str(e)})
    
@app.route('/authenticate', methods=['POST'])
def authenticate_patient():
    try:
        data = request.get_json()
        aadhar_no = data['aadhar_no']
        abha_id = data['abha_id']

        user_ipfs_hash = user_ipfs_mapping.get(abha_id)

        if user_ipfs_hash:
            return jsonify({'authenticate': True})
        
        else:
            return jsonify({'authenticated': False, 'message': 'User not found'})
    except Exception as e:
        return jsonify({'error': str(e)})