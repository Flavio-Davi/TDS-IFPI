import 'package:flutter/material.dart';
import 'package:sqflite/sqflite.dart';
import 'package:path/path.dart' show join;
import 'package:google_maps_flutter/google_maps_flutter.dart';
import 'package:geolocator/geolocator.dart';
import 'package:url_launcher/url_launcher.dart';

// =============================================================================
// 0️⃣ GERENCIADOR DO BANCO DE DADOS (SQLite)
// =============================================================================
class DatabaseHelper {
  static final DatabaseHelper _instance = DatabaseHelper._internal();
  factory DatabaseHelper() => _instance;
  DatabaseHelper._internal();

  static Database? _database;

  Future<Database> get database async {
    if (_database != null) return _database!;
    _database = await _initDatabase();
    return _database!;
  }

  Future<Database> _initDatabase() async {
    String path = join(await getDatabasesPath(), 'app_database.db');
    return await openDatabase(
      path,
      version: 1,
      onCreate: (db, version) {
        return db.execute(
          'CREATE TABLE users(id INTEGER PRIMARY KEY AUTOINCREMENT, email TEXT UNIQUE, password TEXT)',
        );
      },
    );
  }

  Future<int> registerUser(String email, String password) async {
    final db = await database;
    try {
      return await db.insert(
        'users',
        {'email': email, 'password': password},
        conflictAlgorithm: ConflictAlgorithm.abort,
      );
    } catch (e) {
      return -1;
    }
  }

  Future<bool> loginUser(String email, String password) async {
    final db = await database;
    final List<Map<String, dynamic>> maps = await db.query(
      'users',
      where: 'email = ? AND password = ?',
      whereArgs: [email, password],
    );
    return maps.isNotEmpty;
  }

  Future<int> updatePassword(String email, String newPassword) async {
    final db = await database;
    return await db.update(
      'users',
      {'password': newPassword},
      where: 'email = ?',
      whereArgs: [email],
    );
  }
}

// =============================================================================
// MODELO DE DADOS DE CONTATO (COM ENDEREÇO)
// =============================================================================
class Contact {
  int id;
  String name;
  String email;
  String phone;
  String address; // CAMPO NOVO

  Contact({
    required this.id, 
    required this.name, 
    required this.email, 
    required this.phone,
    required this.address, // CAMPO NOVO
  });
}

class ContactRepository {
  static final List<Contact> _contacts = [
    Contact(
      id: 1, 
      name: 'João Silva', 
      email: 'joao@exemplo.com', 
      phone: '11987654321',
      address: 'Rua Alcides Freitas, 665, Matinha, Teresina-PI'
    ),
    Contact(
      id: 2, 
      name: 'Maria Souza', 
      email: 'maria@exemplo.com', 
      phone: '21998765432',
      address: 'Av. Frei Serafim, 1000, Centro, Teresina-PI'
    ),
  ];
  static int _nextId = 3;
  
  static List<Contact> getAll() => _contacts;
  
  static void add(Contact contact) {
    contact.id = _nextId++;
    _contacts.add(contact);
  }
  
  static void update(Contact updatedContact) {
    final index = _contacts.indexWhere((c) => c.id == updatedContact.id);
    if (index != -1) {
      _contacts[index] = updatedContact;
    }
  }
  
  static void delete(int id) {
    _contacts.removeWhere((c) => c.id == id);
  }
}

// =============================================================================
// DEFINIÇÃO DE ROTAS E MAIN
// =============================================================================
const String loginRoute = '/';
const String homeRoute = '/home';
const String contactsRoute = '/contacts';
const String contactFormRoute = '/contact-form';
const String mapRoute = '/map';

void main() {
  WidgetsFlutterBinding.ensureInitialized(); 
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'App Didático Flutter',
      theme: ThemeData(
        primarySwatch: Colors.blue,
        floatingActionButtonTheme: const FloatingActionButtonThemeData(
          backgroundColor: Colors.blue,
          foregroundColor: Colors.white,
        ),
      ),
      initialRoute: loginRoute,
      routes: {
        loginRoute: (context) => const LoginScreen(),
        homeRoute: (context) => const HomeScreen(),
        contactsRoute: (context) => const ContactListScreen(),
        contactFormRoute: (context) => const ContactFormScreen(),
        mapRoute: (context) => const MapScreen(),
      },
    );
  }
}

// =============================================================================
// 1️⃣ TELA DE LOGIN (COM IMAGEM LOCAL)
// =============================================================================
class LoginScreen extends StatefulWidget {
  const LoginScreen({super.key});
  @override
  State<LoginScreen> createState() => _LoginScreenState();
}

class _LoginScreenState extends State<LoginScreen> {
  final _emailController = TextEditingController();
  final _passwordController = TextEditingController();
  final DatabaseHelper _dbHelper = DatabaseHelper();

  void _handleLogin() async {
    String email = _emailController.text;
    String pass = _passwordController.text;
    if (email.isEmpty || pass.isEmpty) {
      ScaffoldMessenger.of(context).showSnackBar(const SnackBar(content: Text('Preencha e-mail e senha')));
      return;
    }
    bool success = await _dbHelper.loginUser(email, pass);
    if (success) {
      if (!mounted) return;
      Navigator.of(context).pushReplacementNamed(homeRoute);
    } else {
      if (!mounted) return;
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(content: Text('Usuário ou senha inválidos!'), backgroundColor: Colors.red),
      );
    }
  }

  void _showRegisterDialog() {
    final emailCtrl = TextEditingController();
    final passCtrl = TextEditingController();
    showDialog(
      context: context,
      builder: (context) => AlertDialog(
        title: const Text("Criar Nova Conta"),
        content: Column(
          mainAxisSize: MainAxisSize.min,
          children: [
            TextField(controller: emailCtrl, decoration: const InputDecoration(labelText: "E-mail")),
            TextField(controller: passCtrl, decoration: const InputDecoration(labelText: "Senha"), obscureText: true),
          ],
        ),
        actions: [
          TextButton(onPressed: () => Navigator.pop(context), child: const Text("Cancelar")),
          ElevatedButton(
            onPressed: () async {
              if (emailCtrl.text.isNotEmpty && passCtrl.text.isNotEmpty) {
                int result = await _dbHelper.registerUser(emailCtrl.text, passCtrl.text);
                if (!mounted) return;
                Navigator.pop(context);
                if (result != -1) {
                   ScaffoldMessenger.of(context).showSnackBar(const SnackBar(content: Text('Conta criada! Faça login.')));
                } else {
                   ScaffoldMessenger.of(context).showSnackBar(const SnackBar(content: Text('E-mail já cadastrado!'), backgroundColor: Colors.red));
                }
              }
            },
            child: const Text("Cadastrar"),
          )
        ],
      ),
    );
  }

  void _showRecoverDialog() {
    final emailCtrl = TextEditingController();
    final newPassCtrl = TextEditingController();
    showDialog(
      context: context,
      builder: (context) => AlertDialog(
        title: const Text("Redefinir Senha"),
        content: Column(
          mainAxisSize: MainAxisSize.min,
          children: [
            const Text("Digite seu e-mail e a NOVA senha.", style: TextStyle(fontSize: 12, color: Colors.grey)),
            const SizedBox(height: 10),
            TextField(controller: emailCtrl, decoration: const InputDecoration(labelText: "Seu E-mail")),
            TextField(controller: newPassCtrl, decoration: const InputDecoration(labelText: "Nova Senha"), obscureText: true),
          ],
        ),
        actions: [
          TextButton(onPressed: () => Navigator.pop(context), child: const Text("Cancelar")),
          ElevatedButton(
            onPressed: () async {
              int rowsAffected = await _dbHelper.updatePassword(emailCtrl.text, newPassCtrl.text);
              if (!mounted) return;
              Navigator.pop(context);
              if (rowsAffected > 0) {
                ScaffoldMessenger.of(context).showSnackBar(const SnackBar(content: Text('Senha atualizada com sucesso!')));
              } else {
                ScaffoldMessenger.of(context).showSnackBar(const SnackBar(content: Text('E-mail não encontrado.'), backgroundColor: Colors.red));
              }
            },
            child: const Text("Alterar Senha"),
          )
        ],
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Login'), automaticallyImplyLeading: false),
      body: Center(
        child: SingleChildScrollView(
          padding: const EdgeInsets.all(32.0),
          child: Column(
            children: <Widget>[
              // --- IMAGEM LOCAL AQUI ---
              Image.asset(
                'assets/images/topo_ifpi.png',
                height: 100,
              ),
              const SizedBox(height: 32.0),
              
              const Text('Bem-vindo!', style: TextStyle(fontSize: 24, fontWeight: FontWeight.bold)),
              const SizedBox(height: 32.0),
              TextFormField(controller: _emailController, decoration: const InputDecoration(labelText: 'E-mail', border: OutlineInputBorder(), prefixIcon: Icon(Icons.email)), keyboardType: TextInputType.emailAddress),
              const SizedBox(height: 16.0),
              TextFormField(controller: _passwordController, decoration: const InputDecoration(labelText: 'Senha', border: OutlineInputBorder(), prefixIcon: Icon(Icons.lock)), obscureText: true),
              const SizedBox(height: 32.0),
              SizedBox(width: double.infinity, child: ElevatedButton(onPressed: _handleLogin, style: ElevatedButton.styleFrom(padding: const EdgeInsets.symmetric(vertical: 16.0)), child: const Text('Entrar'))),
              const SizedBox(height: 16.0),
              Row(mainAxisAlignment: MainAxisAlignment.center, children: [
                TextButton(onPressed: _showRecoverDialog, child: const Text('Recuperar senha')),
                const Text(' | '),
                TextButton(onPressed: _showRegisterDialog, child: const Text('Criar conta')),
              ]),
            ],
          ),
        ),
      ),
    );
  }
}

// =============================================================================
// 2️⃣ TELA PRINCIPAL (COM IMAGEM LOCAL)
// =============================================================================
class HomeScreen extends StatelessWidget {
  const HomeScreen({super.key});
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Principal'), automaticallyImplyLeading: false),
      body: Center(
        child: Padding(
          padding: const EdgeInsets.all(32.0),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: <Widget>[
              // --- IMAGEM LOCAL AQUI ---
              Center(
                child: Image.asset(
                  'assets/images/topo_ifpi.png',
                  height: 120,
                ),
              ),
              const SizedBox(height: 40.0),

              _HomeButton(text: 'Localização Real', icon: Icons.map, onPressed: () => Navigator.of(context).pushNamed(mapRoute)),
              const SizedBox(height: 24.0),
              _HomeButton(text: 'Listar Contatos', icon: Icons.people, onPressed: () => Navigator.of(context).pushNamed(contactsRoute)),
            ],
          ),
        ),
      ),
    );
  }
}

class _HomeButton extends StatelessWidget {
  final String text;
  final IconData icon;
  final VoidCallback onPressed;
  const _HomeButton({required this.text, required this.icon, required this.onPressed});
  @override
  Widget build(BuildContext context) {
    return ElevatedButton.icon(
      onPressed: onPressed,
      icon: Icon(icon, size: 40),
      label: Padding(padding: const EdgeInsets.symmetric(vertical: 20.0), child: Text(text, style: const TextStyle(fontSize: 20))),
      style: ElevatedButton.styleFrom(
        foregroundColor: Colors.white,
        backgroundColor: Theme.of(context).primaryColor,
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
      ),
    );
  }
}

// =============================================================================
// 3️⃣ TELA DE MAPA (COM PINO VERMELHO)
// =============================================================================
class MapScreen extends StatefulWidget {
  const MapScreen({super.key});

  @override
  State<MapScreen> createState() => _MapScreenState();
}

class _MapScreenState extends State<MapScreen> {
  late GoogleMapController mapController;
  Set<Marker> _markers = {}; // LISTA DE MARCADORES (PINOS)
  
  final LatLng _initialPosition = const LatLng(-14.235004, -51.92528);
  bool _isLoading = true;

  @override
  void initState() {
    super.initState();
    _determinePosition();
  }

  Future<void> _determinePosition() async {
    bool serviceEnabled;
    LocationPermission permission;

    serviceEnabled = await Geolocator.isLocationServiceEnabled();
    if (!serviceEnabled) {
      _stopLoading();
      ScaffoldMessenger.of(context).showSnackBar(const SnackBar(content: Text('Ative o GPS do celular.')));
      return;
    }

    permission = await Geolocator.checkPermission();
    if (permission == LocationPermission.denied) {
      permission = await Geolocator.requestPermission();
      if (permission == LocationPermission.denied) {
        _stopLoading();
        return;
      }
    }

    if (permission == LocationPermission.deniedForever) {
      _stopLoading();
      return;
    }

    Position position = await Geolocator.getCurrentPosition();
    LatLng userPosition = LatLng(position.latitude, position.longitude);

    if(mounted) {
      setState(() {
        // CRIA O PINO VERMELHO
        _markers.add(
          Marker(
            markerId: const MarkerId('current_location'),
            position: userPosition,
            infoWindow: const InfoWindow(title: 'Você está aqui!'),
            icon: BitmapDescriptor.defaultMarker, 
          ),
        );
        _isLoading = false;
      });
    }

    mapController.animateCamera(
      CameraUpdate.newCameraPosition(
        CameraPosition(
          target: userPosition,
          zoom: 18,
        ),
      ),
    );
  }

  void _stopLoading() {
    if(mounted) setState(() => _isLoading = false);
  }

  void _onMapCreated(GoogleMapController controller) {
    mapController = controller;
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Minha Localização')),
      body: Stack(
        children: [
          GoogleMap(
            onMapCreated: _onMapCreated,
            initialCameraPosition: CameraPosition(
              target: _initialPosition,
              zoom: 4,
            ),
            markers: _markers, // EXIBE O PINO
            myLocationEnabled: true,
            myLocationButtonEnabled: true,
          ),
          if (_isLoading)
            const Center(
              child: CircularProgressIndicator(),
            ),
        ],
      ),
    );
  }
}

// =============================================================================
// DEMAIS TELAS (Lista de Contatos COM ROTA e Formulário COM ENDEREÇO)
// =============================================================================
class ContactListScreen extends StatefulWidget {
  const ContactListScreen({super.key});
  @override
  State<ContactListScreen> createState() => _ContactListScreenState();
}
class _ContactListScreenState extends State<ContactListScreen> {
  void _refreshContacts() { setState(() {}); }
  
  void _deleteContact(int id) {
    ContactRepository.delete(id);
    _refreshContacts();
  }

  // --- FUNÇÃO PARA ABRIR O GOOGLE MAPS ---
  Future<void> _openMapRoute(String address) async {
    final query = Uri.encodeComponent(address);
    final googleUrl = Uri.parse("https://www.google.com/maps/search/?api=1&query=$query");

    try {
      await launchUrl(googleUrl, mode: LaunchMode.externalApplication);
    } catch (e) {
      if(!mounted) return;
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(content: Text('Não foi possível abrir o mapa.')),
      );
    }
  }

  @override
  Widget build(BuildContext context) {
    final contacts = ContactRepository.getAll();
    return Scaffold(
      appBar: AppBar(title: const Text('Contatos')),
      body: contacts.isEmpty
          ? const Center(child: Text('Nenhum contato cadastrado.'))
          : ListView.builder(
              itemCount: contacts.length,
              itemBuilder: (context, index) {
                final contact = contacts[index];
                return Card(
                  margin: const EdgeInsets.symmetric(horizontal: 10, vertical: 5),
                  child: ListTile(
                    title: Text(contact.name, style: const TextStyle(fontWeight: FontWeight.bold)),
                    subtitle: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Text(contact.email),
                        Text(contact.address, style: const TextStyle(fontSize: 12, color: Colors.grey)),
                      ],
                    ),
                    isThreeLine: true,
                    trailing: Row(
                      mainAxisSize: MainAxisSize.min,
                      children: [
                          // BOTÃO DE ROTA
                          IconButton(
                            icon: const Icon(Icons.directions, color: Colors.blue, size: 30),
                            onPressed: () => _openMapRoute(contact.address),
                          ),
                          IconButton(icon: const Icon(Icons.edit), onPressed: () async { await Navigator.of(context).pushNamed(contactFormRoute, arguments: contact); _refreshContacts(); }),
                          IconButton(icon: const Icon(Icons.delete, color: Colors.red), onPressed: () => _deleteContact(contact.id)),
                      ],
                    ),
                  ),
                );
              },
            ),
      floatingActionButton: FloatingActionButton(
        onPressed: () async { await Navigator.of(context).pushNamed(contactFormRoute); _refreshContacts(); },
        child: const Icon(Icons.add),
      ),
    );
  }
}

class ContactFormScreen extends StatefulWidget {
  const ContactFormScreen({super.key});
  @override
  State<ContactFormScreen> createState() => _ContactFormScreenState();
}
class _ContactFormScreenState extends State<ContactFormScreen> {
  final _formKey = GlobalKey<FormState>();
  final _nameController = TextEditingController();
  final _emailController = TextEditingController();
  final _phoneController = TextEditingController();
  final _addressController = TextEditingController(); // CAMPO ENDEREÇO
  Contact? _editingContact;

  @override
  void didChangeDependencies() {
    super.didChangeDependencies();
    final contact = ModalRoute.of(context)?.settings.arguments as Contact?;
    if (contact != null && _editingContact == null) {
      _editingContact = contact;
      _nameController.text = contact.name;
      _emailController.text = contact.email;
      _phoneController.text = contact.phone;
      _addressController.text = contact.address; // CARREGA ENDEREÇO
    }
  }

  void _saveContact() {
    if (_formKey.currentState!.validate()) {
      final newContact = Contact(
        id: _editingContact?.id ?? 0, 
        name: _nameController.text, 
        email: _emailController.text, 
        phone: _phoneController.text,
        address: _addressController.text // SALVA ENDEREÇO
      );

      if (_editingContact == null) { ContactRepository.add(newContact); } else { ContactRepository.update(newContact); }
      Navigator.of(context).pop();
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text(_editingContact != null ? 'Editar' : 'Novo')),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(24.0),
        child: Form(key: _formKey, child: Column(children: [
          TextFormField(controller: _nameController, decoration: const InputDecoration(labelText: 'Nome'), validator: (v) => v!.isEmpty ? 'Erro' : null),
          TextFormField(controller: _emailController, decoration: const InputDecoration(labelText: 'Email'), validator: (v) => v!.isEmpty ? 'Erro' : null),
          TextFormField(controller: _phoneController, decoration: const InputDecoration(labelText: 'Telefone'), validator: (v) => v!.isEmpty ? 'Erro' : null),
          const SizedBox(height: 10),
          // CAMPO DE ENDEREÇO
          TextFormField(
            controller: _addressController, 
            decoration: const InputDecoration(labelText: 'Endereço', border: OutlineInputBorder()), 
            maxLines: 2,
            validator: (v) => v!.isEmpty ? 'Necessário para Rota' : null
          ),
          const SizedBox(height: 20),
          ElevatedButton(onPressed: _saveContact, child: const Text('Salvar'))
        ])),
      ),
    );
  }
}