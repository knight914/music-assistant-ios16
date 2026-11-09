# Experimental iOS 16 build

Based on Music Assistant mobile-app upstream commit `5bc05d0b6ab3f936fff95166815e6daba3c1600c`; original source and license retained. This is an unofficial experiment, not a verified working port.

The app deployment target is lowered from 18.5 to 16.0, and the WebRTC build phase respects CODE_SIGNING_ALLOWED=NO. The manually dispatched iOS 16 workflow attempts an unsigned device build and packages Payload as IPA. No successful build or device test is claimed; unsupported APIs, binary minimum OS versions, dependency requirements and runtime behavior remain to be investigated using real compiler output and device testing. Manual workflow dispatch requires the workflow file to exist on the repository default branch; select the work branch in the dispatch UI after that prerequisite is met.

The IPA is not Apple-signed. TrollStore's installation and signing treatment, nested framework entitlements, CarPlay entitlements, and the device/OS exploit compatibility must be verified independently. Do not assume CarPlay works. The workflow does not install or deploy.
