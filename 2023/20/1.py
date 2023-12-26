def read_lines_from_file(file_path):
	with open(file_path) as f:
		return f.readlines()
	
class FlipFlop:
	def __init__(self, label, destination_module_labels):
		self.label = label
		self.status = 'off'
		self.destination_module_labels = destination_module_labels

	def __str__(self):
		return f'FlipFlop "{self.label}": {self.status}'
	
	def receive_pulse(self, input_pulse):
		output_pulse = None
		if input_pulse == 'high':
			pass
		elif input_pulse == 'low':
			if self.status == 'off':
				self.status = 'on'
				output_pulse = 'high'
			elif self.status == 'on':
				self.status = 'off'
				output_pulse = 'low'
			else:
				raise 'dumb'
		
		return output_pulse

	def send_pulse(self, all_modules):
		for destination_module_label in self.destination_module_labels:
			destination_module = all_modules[destination_module_label]
		pass

class Conjunction:
	def __init__(self, label, destination_module_labels):
		self.label = label
		self.destination_module_labels = destination_module_labels
		self.memory = {}

	def receive_pulse(self, input_pulse, input_pulse_from):
		if len(self.memory.keys()) == 0:
			raise "initialize default memory first"
		
		self.memory[input_pulse_from] = input_pulse
		output_pulse = 'high'
		if all(pulse == 'high' for pulse in self.memory.values()):
			output_pulse = 'low'
		
		return output_pulse
	
	def init_default_memory(self, input_module_labels):
		self.memory = {label: 'low' for label in input_module_labels}


class Broadcaster:
		def __init__(self, label, destination_module_labels):
			self.label = label
			self.destination_module_labels = destination_module_labels

		def receive_pulse(self, input_pulse):
			output_pulse = input_pulse
			return output_pulse
		

def solve(file_path):
	module_config = read_lines_from_file(file_path)

	all_modules = {}
	for module_str in module_config:
		module_str, destinations_str = module_str.split(' -> ')
		destination_module_labels = destinations_str.split(', ')
		module = None
		module_label = None
		if (module_str == 'broadcaster'):
			module_label = 'broadcaster'
			module = Broadcaster(label='broadcaster', destination_module_labels=destination_module_labels)
		elif (module_str.startswith('%')):
			module_label = module_str[1::]
			module = FlipFlop(label=module_label, destination_module_labels=destination_module_labels)
		elif (module_str.startswith('&')):
			module_label = module_str[1::]
			module = Conjunction(label=module_label, destination_module_labels=destination_module_labels)
		else:
			raise "unknown module type"
		
		all_modules[module_label] = module


	print(all_modules)
	# print(f'[{file_path}]: {calibration_value}')

solve('sample.txt')
# solve('input.txt')
