from flask import Flask, request, Response, jsonify
from ...Site import site, main_form_subject
from ..entities.MainFormData import MainFormData as FormData
from ..features.MainForm.MainFormValidator import MainFormValidator

@site.route('/', methods=['POST'])
def handle():
    '''
      Main form data validation
    '''
    # Initiate validator instance
    validator = MainFormValidator()
    # Pass data to validator
    validator.validate(request.form)
    # Return error if data is not valid
    if not validator.is_valid:
        return jsonify(validator.error_message), 400
    # Create form data instance
    main_form_data = FormData(request.form)
    # Pass data to Subject
    main_form_subject.updateFormData(main_form_data)

    return 'success', 200