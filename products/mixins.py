from rest_framework_simplejwt.exceptions import InvalidToken
from rest_framework.status import HTTP_401_UNAUTHORIZED
from django.http import JsonResponse


class CourseAccesMixin:
    def dispatch(self, request, *args, **kwargs):
            try:
                req = self.initialize_request(request, *args, **kwargs)
                print(req.user)
                if not request.user.is_authenticated:
                    return JsonResponse(
                        {"details": "Authentication credentials were not provided."},
                        status=HTTP_401_UNAUTHORIZED
                    )
                subscription = request.user.subscription
                pricing_tier = subscription.pricing.name
                tiers = [
                    'Basic Plan',
                    'Pro Plan',
                    'Premium Plan',
                ]
                if not pricing_tier in tiers:
                    return JsonResponse({"details":"Upgrade Your pricing"}, status=401)
                return super().dispatch(request, *args, **kwargs)
            except Exception as e:
                return JsonResponse(
                    {
                        "error": {
                            'message': str(e)
                        }
                    },
                    status=HTTP_401_UNAUTHORIZED
            )