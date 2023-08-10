document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('registration-form');
    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const name = document.getElementById('name').value;
        const age = document.getElementById('age').value;
        const gender = document.getElementById('gender').value;
        const aadhar_no = document.getElementById('aadhar_no').value;
        const abha_id = document.getElementById('abha_id').value;
        const phone_no = document.getElementById('phone_no').value;
        
        try {
            const response = await fetch('/register', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    name,
                    age,
                    gender,
                    aadhar_no,
                    abha_id,
                    phone_no
                })
            });
            
            const data = await response.json();
            alert(`Patient registered with IPFS hash: ${data.ipfs_hash}`);
            
            // You can now display the IPFS hash to the user or perform other actions
        } catch (error) {
            console.error('Error registering patient:', error);
        }
    });
});
