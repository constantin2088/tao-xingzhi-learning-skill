"""Conservative labels for recorded practice, not psychometric assessment."""
def classify(evidence):
 keys=('completed','independent','transfer_success')
 if not isinstance(evidence,dict) or any(type(evidence.get(k)) is not bool for k in keys):raise ValueError('three explicit boolean observations required')
 if evidence['transfer_success'] and not (evidence['completed'] and evidence['independent']):raise ValueError('inconsistent transfer claim')
 if not evidence['completed']:return 'needs_practice'
 if not evidence['independent']:return 'supported_completion'
 if not evidence['transfer_success']:return 'independent_same_task'
 return 'observed_transfer'
