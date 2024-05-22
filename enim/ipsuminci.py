def approve_dpx():
    """Approve the DPX."""

    # TODO(developer): Uncomment and set the following variables
    # project_id = 'PROJECT_ID_HERE'
    # location = 'LOCATION_HERE'
    # dpx_id = 'DPX_ID_HERE'

    client = dataplex_v1.MetadataServiceClient()

    # The full resource name of the DPX
    name = client.data_path_explorer_path(project_id, location, dpx_id)

    operation = client.approve_data_path_explorer(name=name)
    result = operation.result()

    print("Approved DPX: {}".format(result.name))

  
