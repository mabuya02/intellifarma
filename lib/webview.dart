import 'package:flutter/material.dart';
import 'package:share_plus/share_plus.dart';
import 'package:webview_flutter/webview_flutter.dart';

class VideoWebview extends StatefulWidget {
  const VideoWebview(
      {super.key, required this.videoLink, required this.cropType});
  final String videoLink;
  final String cropType;

  @override
  State<VideoWebview> createState() => _VideoWebviewState();
}

class _VideoWebviewState extends State<VideoWebview> {
  late final WebViewController webviewController;

  @override
  void initState() {
    super.initState();
    webviewController = WebViewController()
      ..setJavaScriptMode(JavaScriptMode.unrestricted)
      ..setBackgroundColor(const Color(0x00000000))
      ..setNavigationDelegate(
        NavigationDelegate(
          onProgress: (int progress) {
            Center(
              child: CircularProgressIndicator(
                value: progress / 100,
                color: Theme.of(context).colorScheme.secondary,
              ),
            );
          },
          onPageStarted: (String url) {
            Center(
              child: CircularProgressIndicator(
                color: Theme.of(context).colorScheme.secondary,
              ),
            );
          },
          onPageFinished: (String url) {},
          onWebResourceError: (WebResourceError error) {
            const Center(
              child: CircularProgressIndicator(
                color: Colors.red,
              ),
            );
          },
          // onNavigationRequest: (NavigationRequest request) {
          //   if (request.url.startsWith('https://www.google.com/')) {
          //     return NavigationDecision.prevent;
          //   }
          //   return NavigationDecision.navigate;
          // },
        ),
      )
      ..loadRequest(
        Uri.parse(widget.videoLink),
      );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        leading: IconButton(
          onPressed: () {
            webviewController.canGoBack().then((value) {
              if (value) {
                webviewController.goBack();
              } else {
                Navigator.pop(context);
              }
            });
          },
          icon: const Icon(
            Icons.cancel,
            color: Colors.white,
          ),
        ),
        actions: [
          IconButton(
            onPressed: () {
              webviewController.reload();
            },
            icon: const Icon(
              Icons.refresh,
              color: Colors.white,
            ),
          ),
          IconButton(
              onPressed: () {
                Share.share(
                    'Check out ${widget.cropType} Farming ${widget.videoLink}');
              },
              icon: const Icon(
                Icons.share,
                color: Colors.white,
              )),
        ],
        title: Text(
          '${widget.cropType} Farming',
          style: const TextStyle(
              color: Colors.white, fontSize: 20.0, fontWeight: FontWeight.w500),
        ),
        backgroundColor: Theme.of(context).colorScheme.secondary,
      ),
      body: WebViewWidget(
        controller: webviewController,
      ),
    );
  }
}
